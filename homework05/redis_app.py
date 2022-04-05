#!/usr/bin/python3 
# 
# desc: An app that returns meteorite landing data from a redis server
# 
# Date created: 4/4/2022
# 
import redis
from flask import Flask, request
import json
import os
import logging


app = Flask(__name__)

posted = False

@app.route('/data', methods=['GET', 'POST'])
def data():
    '''                                                                                                                 
    Updates/Returns the meteorite landing data found from:

        https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json     

    Post: updates the data in the redis database
    Get: returns the data                                                              
                                                                                                                        
    Args:                                                                                                               
        None                                                                                                            
                                                                                                                        
    Returns:                                                                                                            
        (str): POST or GET message                                                                                      
    '''
    global posted
    rd = redis.Redis(host='172.17.0.27', port=6379, db=11)

    if request.method == 'POST':
        data_downloaded = os.path.exists('ML_Data_Sample.json')
        if data_downloaded:
            logging.debug('data is present in working directory. Will update database based on present data')
            with open('ML_Data_Sample.json', 'r') as f:
                json_set = json.load(f)
                rd.set("meteorite data", json.dumps(json_set))
                posted = True
                # NOTE: if I were to use separate keys for each data point, this should work
                # elem_count = 0
                # for elem in json_set:
                #     rd.set(f'data{elem_count}', json.dumps(elem))
                #     elem_count += 1
            return f'Data has been updated\n'
        else:
            logging.warning('data set is not loaded into the server')         
            return f'data set is not loaded into the server\n'
    else:
        # GET method
        if posted:
            data = json.loads(rd.get("meteorite data"))
            return data
        else:
            return '''first run the command 
            curl -X POST localhost:5011/data\n'''




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





