from flask import Flask, escape, request, jsonify

app = Flask(__name__)

STUDENTS = ['John Doe', 'Mary Doe', 'Bob Doe']
CLASSES = {}
CLASSID = 0

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/students', methods = ['POST'])
def createStudent():
    STUDENTS.append(request.form['name'])
    return jsonify({
        'id' : str(len(STUDENTS) - 1),
        'name' : request.form['name']
    }), 201

@app.route('/students/<id>', methods = ['GET'])
def getStudents(id):
    return jsonify({
        'id': id,
        'name': STUDENTS[int(id)],
    })

@app.route('/classes', methods = ['POST'])
def createClass():
    global CLASSID
    CLASSES[CLASSID] = {}
    CLASSES[CLASSID]['name'] = request.form['name']
    CLASSES[CLASSID]['students'] = []
    CLASSID += 1
    return jsonify({
        'id' : CLASSID - 1,
        'name' : request.form['name'],
        'students' : CLASSES[CLASSID - 1]['students']
    }), 201

@app.route('/classes/<id>', methods = ['GET'])
def getClass(id):
    return jsonify({
        'id' : id,
        'name' : CLASSES[int(id)]['name'],
        'students' : CLASSES[int(id)]['students']
    })

@app.route('/classes/<id>', methods = ['PATCH'])
def patchClass(id):
    CLASSES[int(id)]['students'].append(STUDENTS[int(request.form['student_id'])])
    students = []
    for student in CLASSES[int(id)]['students']:
        students.append({
            'id' : STUDENTS.index(student),
            'name' : student
        })
    
    return jsonify({
        'id' : id,
        'name' : CLASSES[int(id)]['name'],
        'students' : students
    })