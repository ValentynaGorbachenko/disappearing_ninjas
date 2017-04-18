from flask import Flask, request, render_template, redirect, render_template_string
app = Flask(__name__)
app.secret_key = "\xe8\xd5\x9e\x1f\x9da\x94\xe5\x88\\%\xde\xa6\xab\xca\x81\x1a\xd8\x0e\xacl\x94U\xd1"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def all_ninjas():
	print "inside the ninjas"
	return render_template('partials/_all_ninjas.html')

@app.route('/ninjas/<color>')
def ninjas_by_color(color):
	print color
	ninja_colors ={
		'red': {'name': 'Raphael', 'path': 'img/raphael.jpg'},
		'blue': {'name': 'Leonardo', 'path': 'img/leonardo.jpg'},
		'orange': {'name': 'Michelangelo', 'path': 'img/michelangelo.jpg'},
		'purple': {'name': 'Donatello', 'path': 'img/donatello.jpg'},
		'other': {'name': 'Not April', 'path': 'img/notapril.jpg'}
	}
	data = {}
	if color in ninja_colors:
		print "hey there"
		data['path'] = ninja_colors[color]['path']
		data['name'] = ninja_colors[color]['name']
		print data
	else:
		data['path'] = ninja_colors['other']['path']
		data['name'] = ninja_colors['other']['name'];
	print data
	return render_template('partials/_by_color.html', data = data)

app.run(debug=True)