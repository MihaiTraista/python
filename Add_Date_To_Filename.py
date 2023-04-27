# after importing all voice memos from iPhone, run this to prepend the date to the name of each file

import os
import datetime

dir_path = '/Users/mihaitraista/Desktop/test'

for file_name in os.listdir(dir_path):
    if file_name.endswith('.m4a'):  # Only process m4a files (iOS voice memos)
        file_path = os.path.join(dir_path, file_name)
        file_stat = os.stat(file_path)
        create_time = file_stat.st_mtime  # Unix format
        create_date = datetime.datetime.fromtimestamp(create_time).strftime('%Y-%m-%d')  # date string
