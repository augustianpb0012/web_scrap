# app/utils.py
import re

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?'  # http:// or https://
        r'([\w\-]+\.)+[\w\-]+'  # Domain name
        r'(:\d+)?(\/.*)?$'  # Optional port and path
    )
    return bool(pattern.match(url))
