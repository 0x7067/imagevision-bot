#!/usr/bin/env python3

import requests
import operator
import time

# Variables

_msurl = 'https://api.projectoxford.ai/vision/v1.0/analyze'
_mskey = '' # YOUR Microsoft Computer Vision API token here
_msMaxNumRetries = 10

def msProcessRequest( json, data, headers, params ):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _msurl, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 
            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _msMaxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
        
    return result


if __name__ == '__main__':
    main()
