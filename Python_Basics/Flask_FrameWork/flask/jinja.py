'''
Building the URL Dynamically
Variable rule
Jinja 2 Template engine
'''

## Jinja 2 Template engine
'''
{{  }} expression to print output in html
{%...%} coditions, for loops etc
{#...#} this is for comments
'''

from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome to Flask framework</h1></html>"


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=="POST":
        name = request.form['name']
        wish = request.form['wish']
        return f"Hello {name}! is saying {wish}"
    else:
        render_template("form.html")

#Variable rule
@app.route('/success/<int:score>')   # By default the value we are passing is a String
def success(score):
    res=""
    if score > 50:
        res="PASSED"
    else:
        res ="FAILED"
    
    return render_template('result.html',results=res)

@app.route('/success_res/<int:score>')   # By default the value we are passing is a String
def success_res(score):
    res=""
    if score > 50:
        res="PASSED"
    else:
        res ="FAILED"
    
    exp={'score':score,"res":res}
    
    return render_template('result1.html',results=exp)

# If condition
@app.route('/success_if/<int:score>')   # By default the value we are passing is a String
def success_if(score):
    return render_template('result2.html',results=score)

@app.route('/marksform',methods=['GET','POST'])
def marksform():
    if request.method == 'POST':
        c = float(request.form['c'])
        java = float(request.form['java'])
        python = float(request.form['python'])
        total_score = (c+java+python)/3
        return redirect(url_for('success_res',score=total_score))
    else:
        return render_template('marksform.html')

if __name__ == "__main__":
    app.run(debug=True)

