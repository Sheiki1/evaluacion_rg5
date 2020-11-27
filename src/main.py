
import csv
from flask import Flask, jsonify

app = Flask(__name__,static_url_path="")

import csv
from flask import Flask, jsonify

app = Flask(__name__,static_url_path="")

@app.route('/', methods=['GET'])
def convert_csv_to_json():
    path = '../data/employees.csv'
    with open (path, 'r') as file:
        reader = csv.reader(file)
        data_list = list()
        for row in reader:
            data_list.append(row)
        data = [dict(zip(data_list[0],row)) for row in data_list]
        data.pop(0)
        s = jsonify(data)
        return s

if __name__== '__main__':
    app.run(debug=True)