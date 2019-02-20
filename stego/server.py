'''
Program: server.py

Description serve up the demo page for my use
as well as the exploit code within the image 

TODO:
	serve the static html (render template)
	serve the static js files to the html
'''

from flask import Flask
from flask import Response
from flask import render_template

app = Flask(__name__)


@app.route('/analysis')
def analysis():
	return render_template('image_layer_analysis.html')
	
# Note: for this route, the server needs to allow cross-
#		origin images and I need to modify:
#			iterative_encoding.html:112
#		in order to set the image origin anonymous
# 		
#		Example:
#			Access-Control-Allow-Origin "*"
@app.route('/encoding')
def encoding():
	resp = Response("Encoding")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/')
def index():
	return """
		<!DOCTYPE html>
		<html>
		<body>
			<h1>Stegosploit Demo Server</h1>
			<ul>
				<li><a href='/'>Home</a></li>
				<li><a href='/analysis'>Image Layer Analysis</a></li>
				<li><a href='/encoding'>Iterative Encoding</a></li>
			</ul>
		</body>
		</html>
		"""

def main():
	app.run(host='localhost',
			port=5000,
			debug=True)

if __name__ == '__main__':
	main()