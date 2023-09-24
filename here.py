from flask import Blueprint
from flask import jsonify
import csv
import json



home_bp = Blueprint('here', __name__)

@home_bp.route('/file1/',methods=['GET'])
def file1():
    csv_file = 'files/file1.csv'

    data = []

    #Read the CSV file and convert it to a list of dictionaries
    with open(csv_file, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
           data.append(row)

    return jsonify(data)

@home_bp.route('/file2/',methods=['GET'])
def file2():
    csv_file = 'files/file2.csv'

    data = []

    #Read the CSV file and convert it to a list of dictionaries
    with open(csv_file, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
           data.append(row)

    return jsonify(data)


@home_bp.route('/file3/',methods=['GET'])
def file3():
    csv_file = 'files/file3.csv'

    data = []

    #Read the CSV file and convert it to a list of dictionaries
    with open(csv_file, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
           data.append(row)

    return jsonify(data)