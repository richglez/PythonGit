from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/') 
def index(): 
#    return "<H1> Home de Mi Sitio </H1> " 
    return render_template('index.html') 


if __name__== '__main__': 
    app.run() 