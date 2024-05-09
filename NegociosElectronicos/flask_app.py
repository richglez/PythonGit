from flask import Flask
app = Flask(_name_)
@app.route("/")
def home():
	return "<p>Home de Mi Sitio"

if _name_ == '_main_':
	app.run()




