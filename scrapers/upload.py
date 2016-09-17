# -*- coding: utf-8 -*-
import boto3
import sys
import os

file_name = sys.argv[1]

# Get the service client
s3 = boto3.client('s3')

# Upload file to youbike-data bucket at key-name
s3.upload_file('data/{}.json'.format(file_name), "youbike-data", file_name)
