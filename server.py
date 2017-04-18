from flask import Flask, request, render_template, redirect 
app = Flask(__name__)
app.secret_key = "\xe8\xd5\x9e\x1f\x9da\x94\xe5\x88\\%\xde\xa6\xab\xca\x81\x1a\xd8\x0e\xacl\x94U\xd1"

@app.route('/')
def index():
	return render_template('index.html')

app.run(debug=True)