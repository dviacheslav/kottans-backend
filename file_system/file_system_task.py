#! /usr/bin/python3.6

import os

path = os.walk(".")

for root, dirs, files in path:
    if "counter.txt" in files: 
        read_file = open("counter.txt", "r")
        data = read_file.read()
        read_file.close()

        try:
            data = int(data)
        except:
            print("No valid data, must be integer...")
            exit(1)
        
        data += 1

        write_file = open("counter.txt", "w")
        write_file.write(str(data))
        write_file.close()
    else:
        create_file = open("counter.txt", "w+")
        create_file.write("1")
        os.chmod("counter.txt", 0o777)
        create_file.close()
