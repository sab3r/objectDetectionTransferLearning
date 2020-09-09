import os
import glob
import pandas as pd
import json
import pickle

def json_to_csv():
    DIR = 'C:/Users/Soham More/DMML2/Datasets/bdd100k_labels_release/bdd100k/labels'
    path_to_json = DIR
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    #path_to_jpeg = 'images/train/'
    #jpeg_files = [pos_jpeg for pos_jpeg in os.listdir(path_to_jpeg) if pos_jpeg.endswith('.jpeg')]
    #fjpeg=(list(reversed(jpeg_files)))
    n=0
    csv_list = []
    labels=[]
    for j in json_files:
        data_file=open('images/train/{}'.format(j))   
        data = json.load(data_file)
        width,height=data['display_width'],data['display_height']
        for item in data:
            file_name = item['name']
            for label in item['labels']:
                #box = item['bounding_box']
                if label['box2d']!='None':
                    category=item['category']
                    labels.append(category)
                    x1=label['box2d']['x1']
                    y1=label['box2d']['y1']
                    x2=label['box2d']['x2']
                    y2=label['box2d']['y2']
                    value = (file_name,
                            category,
                            x1,
                            y1,
                            x2,
                            y2
                            )
                    csv_list.append(value)
        n=n+1
        column_name = ['filename', 'category', 'x1', 'y1', 'x2', 'y2']
        csv_df = pd.DataFrame(csv_list, columns=column_name)
        csv_df.to_csv('{}_labels.csv'.format(j), index=None)
        labels_train=list(set(labels))
        with open("{}_labels.txt".format(j), "wb") as fp:   #Pickling
            pickle.dump(labels_train, fp)
        return "Done"

def main():
    ret = json_to_csv()
    print(ret)
    #csv_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
    print('Successfully converted json to csv.')

main()