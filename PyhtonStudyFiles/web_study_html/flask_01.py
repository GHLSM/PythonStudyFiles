from flask import Flask, request


app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    print(request.form)
    print(request.files)
    file_obj = request.files.get('myfile')
    file_obj.save(file_obj)
    return 'ok'

app.run()
