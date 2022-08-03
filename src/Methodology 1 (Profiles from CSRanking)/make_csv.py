import csv
with open('data.csv', mode='w') as csv_file:
    fieldnames = ['File Name','Author Name','Link','Total Articles Count','Total Citations (Copied)','Total Citations (Calculated)','... Count','Citation Count','False Count','False Citation Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    file=open('author_stats.txt','r')
    data=file.readlines()
    for i in range(0,len(data)-10,11):
        if(len(data)>1):
            writer.writerow({'File Name':data[i],'Author Name':data[i+1],'Link':data[i+2],'Total Articles Count':data[i+3],'Total Citations (Copied)':data[i+4],'Total Citations (Calculated)':data[i+5],'... Count':data[i+6],'Citation Count':data[i+7],'False Count':data[i+8],'False Citation Count':data[i+9]})