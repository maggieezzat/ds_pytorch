import csv
from clean_text import clean_sentence

rootdir = "/data/home/GPUAdmin1/asr/"
files = [rootdir+"train_csvs/M-AILABS_train.csv",rootdir+"train_csvs/cv_train.csv","/speech/german-speechdata-package-v2/SentencesAndIDs.cleaned.txt"]
files_out = [rootdir+"test_csvs/cv_test.csv",rootdir+"dev_csvs/cv_dev.csv",rootdir+"test_csvs/tuda_test.csv",rootdir+"dev_csvs/tuda_dev.csv" ]
sentences = []
for file_dir in files:
    if(".csv" in file_dir):
        with open(file_dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                sentences.append(row[1] +"\n")
    else:
        with open(file_dir, "r") as text:
            for line in text:
                sent = clean_sentence(line.split(" ",1)[1])
                sentences.append(sent+"\n")

sentences_out =[]
for file_dir in files_out:
    with open(file_dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                sentences_out.append(row[1] +"\n")


sent_set = set(sentences)
corpus = open("/data/home/GPUAdmin1/asr/corpus.txt","w")
for sent in sent_set:
    if(sent in sentences_out):
        continue
    corpus.write(sent)

