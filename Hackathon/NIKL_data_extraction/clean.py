import pandas as pd
import csv

# Extracting articles from 조선일보 and 한겨레 for supervised training
# Run this in the same directory as all the other NILK csv files

row_label = ['file_id',	'doc_id',	'title',	'author',	'publisher',	'date',	'topic',	'original_topic',	'sentence_id',	'sentence']
total_files = 38


write_file_name = "dataset.csv"
write_file = open(write_file_name, "a", encoding = "UTF-8", newline = "")
writer = csv.writer(write_file)
for i in range(total_files):
    print("====================")
    print("iter %s" % (i+1))
    print("====================")
    read_file_name = "NIKL_NEWSPAPER_%s.csv" %(i + 1)
    with open(read_file_name, "r", encoding='UTF-8') as read_file:
        reader = csv.reader(read_file)
        counter = 0
        for row in reader:
            if row[4] in ["한겨레", "조선일보사"]:
                writer.writerow(row)
                counter += 1
        print("%s articles found" % counter)
    read_file.close()


write_file.close()




