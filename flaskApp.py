from flask import Flask,jsonify,request
app = Flask(__name__)

tasks = [
    {
        'id':1,
        'name':u'me',
        'contact':u'+91 ...',
        'done':False
    },
    {
        'id':2,
        'name':u'you',
        'contact':u'+91 ...',
        'done':False
    }
]

@app.route("/add-data",methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact'," "),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"succes",
        "message":"task added succefully"
    })
@app.route("/getData")
def getTask():
    return jsonify({
        "data":tasks
    })

if __name__ == '__main__':
    app.run(port = 8000,debug=True)