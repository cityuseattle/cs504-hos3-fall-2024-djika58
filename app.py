from flask import Flask, request
import json

app = Flask(__name__)  # This line creates the Flask app

database = {}
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

from flask import Flask, request
import json

database = {}
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# Create a New Student Record
@app.route('/students', methods=['POST'])
def post_students_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400

# Update an Existing Student Record
@app.route('/students', methods=['PUT'])
def put_students_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400

# Retrieve a Student Record
@app.route('/students/<Student_name>', methods=['GET'])
def get_students_details(Student_name):
    try:
        name = database.get(Student_name)
        if name is None:
            return 'Record Not Found', 404
        else:
            return 'Record Found: ' + Student_name + ' age is ' + str(name), 200
    except KeyError:
        return 'Record Not Found', 404

# Delete a Student Record
@app.route('/students/<Student_name>', methods=['DELETE'])
def delete_students_details(Student_name):
    try:
        if Student_name in database:
            database.pop(Student_name)
            return 'Record deleted successfully', 200
        else:
            return 'Record Not Found', 404
    except Exception as e:
        print("Error while removing record ", e)
        return 'Error while removing record', 400

if __name__ == '__main__':
    app.run(debug=True)

git add .
git commit -m "Submission for Module 3"  
git push
