Description
===========

This repository contains my work on reverse engineering Facebook's GraphQL API.
Several versions of com.facebook.katana are known to distribute the API's schema.
In a binary encoded form.

Using the files provided in this repository one can generate the type information.
Present in the binary representation.

A decoded version is also provided in fb\_graphql\_types.json.
A python module to aid in decoding FlatBuffers binaries is provided in fbs.py.

Instructions
============

To generate the graphql\_types.json file, download Facebook for Android(v230.0.0.36.117).  
Then run `apktool d -r com.facebook.katana.apk`.  
Run `flatc --json --strict-json --raw-binary graph_metadata.fbs -- graph_metadata.bin`.  
graph\_metadata.bin is found in the assets directory.  
And `./schema.py graph_metadata.json >fb_graphql_types.json`.  

Credits
=======
This work has been inspired by [fbchat](https://github.com/fbchat-dev/fbchat).

