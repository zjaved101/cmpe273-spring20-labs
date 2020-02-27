from ariadne import QueryType, ObjectType, MutationType, graphql_sync, make_executable_schema
from ariadne import gql

type_defs = gql("""
    type Query {
        hello: String!
        student(id: ID!): Student!
        classes(id: ID!): Classes!
    }

    type Student {
        id: ID!
        name: String!
    }

    type Classes {
        id: ID!
        name: String!
        students: [Student]!
    }

    type Mutation {
        createStudent(name: String!): Student!
        createClass(name: String!): Classes!
        addStudent(classID: ID!, studentID: ID!): Classes!
    }
""")

query = QueryType()
mutation = MutationType()
student = ObjectType('Student')
classes = ObjectType('Classes')

STUDENTS = ['John Doe', 'Mary Doe', 'Bob Doe']
CLASSES = {}
CLASSID = 0

@query.field("hello")
def resolve_hello(_, info):
    request = info.context
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello World!, %s!" % user_agent

@query.field('student')
def resolve_student(_, info, id):
    return {'id': id, 'name': STUDENTS[int(id)]}

@query.field('classes')
def resolve_classes(_, info, id):
    students = []
    for student in CLASSES[int(id)]['students']:
        students.append({
            'id' : STUDENTS.index(student),
            'name' : student
    })
    return {'id': id, 'name': CLASSES[int(id)]['name'], 'students': students }

@mutation.field('createStudent')
def resolve_createStudent(_, info, name):
    STUDENTS.append(name)
    return {'id': STUDENTS.index(name), 'name': name}

@mutation.field('createClass')
def resolve_createClass(_, info, name):
    global CLASSID
    CLASSES[CLASSID] = {
        'name' : name,
        'students' : []
    }
    CLASSID += 1

    return {'id': CLASSID - 1, 'name': name, 'students': CLASSES[CLASSID-1]['students']}

@mutation.field('addStudent')
def resolve_addStudent(_, info, classID, studentID):
    CLASSES[int(classID)]['students'].append(STUDENTS[int(studentID)])
    students = []
    for student in CLASSES[int(classID)]['students']:
        students.append({
            'id' : STUDENTS.index(student),
            'name' : student
    })
    return {'id': classID, 'name': CLASSES[int(classID)]['name'], 'students': students}

schema = make_executable_schema(type_defs, [query, student, classes, mutation])