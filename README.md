# Flask API for Serving CSV Data as JSON

This repository contains a Flask-based API designed to serve CSV data files in JSON format. It offers endpoints for accessing three different CSV files, each converted into a list of dictionaries and then serialized as JSON objects.

## Features

- **/file1/**: Access data from 'file1.csv' in JSON format.
- **/file2/**: Access data from 'file2.csv' in JSON format.
- **/file3/**: Access data from 'file3.csv' in JSON format.

## How it works

1. The API utilizes Flask, a popular Python web framework, to create routes for each CSV file.
2. CSV data is read and converted into a list of dictionaries using the `csv.DictReader` class.
3. The data is then serialized into JSON format using Flask's `jsonify` function.
4. Users can access the data by sending GET requests to the respective endpoints.

## Why this is useful

- Demonstrates the implementation of a basic Flask API for serving data.
- Offers a simple example of converting CSV data to JSON format, a common data transformation task.
- Provides a foundation for building more complex data APIs and services.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install flask` if not already installed.
3. Run the Flask application with `python app.py`.
4. Access the CSV data as JSON by making GET requests to the specified endpoints.
5. Example program is included as test.py, run this to print the data received 

Feel free to customize and expand upon this codebase to suit your specific data-serving needs or use it as a learning resource for Flask-based API development.

