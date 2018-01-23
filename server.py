from flask import Flask, url_for, render_template
app = Flask(__name__)

# example redirect
# return redirect(url_for('profile', username='John Doe'))

#example logger
# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')

@app.route('/')
def home():
    return render_template('/home/home.html')

@app.route('/backgrounds/<string:category>/<int:frequency>')
def background(category, frequency):
    return "<h1>{} , {}</h1>".format(category, frequency)

@app.route('/sample')
def sample():
    return render_template('/sample/sample.html')