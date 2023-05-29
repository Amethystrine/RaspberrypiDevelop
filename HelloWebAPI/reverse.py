from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/rev',methods=['POST'])
def rev():
    if request.method=='POST':
        text=request.form.get('text')
        res=text[::-1]
        return res

@app.route('/<text>/<text2>')
def indext(text,text2):
    return render_template('reverse.html',text=text+text2)

@app.route('/')
def index():
    return render_template('reverse.html',text='')
    
if __name__=='__main__':
    app.run(debug=True)