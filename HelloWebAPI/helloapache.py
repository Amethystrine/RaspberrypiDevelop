from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello world2"

if __name__=='__main__':
    app.run()

#if __name__=='__main__':
#    app.run()por