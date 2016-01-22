from __future__ import absolute_import
from kwcontributes import app
import requests
import tempfile
import os
import shutil
import contextlib
import gzip
import json

@contextlib.contextmanager
def download_file(url):
    directory = tempfile.mkdtemp()
    local_filename =  os.path.join(directory, url.split('/')[-1])
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


    yield local_filename

    shutil.rmtree(directory)

@app.task
def process_day(url):
    with download_file(url) as file_name:
        with gzip.open(file_name, "rb") as fh:
            for line in fh:
                event = json.loads(line)

    return event
