# src/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>DevOps Zero-Cost Project</h1>
    <p>✅ CI/CD Pipeline Working!</p>
    <p>✅ AWS Free Tier Resources</p>
    <p>✅ Zero Bill Guaranteed</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)