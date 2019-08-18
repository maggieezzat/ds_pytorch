import os
import csv
import time
#given that the worker and server are already running

if(not os.path.exists("/speech/missing2.txt")):
    with open("/home/GPUAdmin1/asr/test.csv","rb") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            os.system("bash /data/home/GPUAdmin1/kaldi/egs/tuda/decode_wav.sh "+ row[0].decode("utf-8-sig"))
            #give the server some time
            #time.sleep(0.25)

else:
    with open("/speech/missing2.txt","r") as f:
        for line in f:
            os.system("bash /data/home/GPUAdmin1/kaldi/egs/tuda/decode_wav.sh "+ line)