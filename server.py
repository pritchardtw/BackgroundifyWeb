from flask import Flask, url_for, render_template
from datetime import datetime
from templates.templates import templates
import logging
logging.basicConfig(filename='server.log', level=logging.DEBUG)
app = Flask(__name__)

# example redirect
# return redirect(url_for('profile', username='John Doe'))

# example logger
# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')

start_time = datetime.now()


@app.route('/')
def home():
    return render_template('/home/home.html')


@app.route('/backgrounds/<string:category>/<int:frequency>')
def background(category, frequency):
    return "<h1>{} , {}</h1>".format(category, frequency)


@app.route('/sample')
def sample():
    current_time = datetime.now()
    td = current_time - start_time
    hours, remainder = divmod(td.seconds, 3600)
    logging.info('Hours: {}'.format(hours))
    # minutes, seconds = divmod(remainder, 60)
    remainder = hours % 8
    logging.info('Remainder: {}'.format(remainder))
    if remainder < 4:
        logging.info('Template 0: {}'.format(templates[0]))
        css_file = templates[0]
    else:
        logging.info('Template 1: {}'.format(templates[1]))
        css_file = templates[1]

    return render_template('/sample/sample.html', css_file='sample/css/{}'.format(css_file))
