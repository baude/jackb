from flask import Flask, render_template, session, request
from gpiozero import LED
import time

app = Flask(__name__)

LIGHT = LED(17)

def _blink(n):
    for secs in range(n):
        LIGHT.on() # on
        time.sleep(.25)
        LIGHT.off() # off
        time.sleep(.25)

@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)


@app.route('/light/on')
def light_on():
    if not LIGHT.is_active:
        LIGHT.on()
        return "turned light on"
    return "light is already on"


@app.route('/light/off')
def light_off():
    if LIGHT.is_active:
        LIGHT.off()
        return "turned light off"
    return "light is already off"


@app.route('/light/status')
def light_status():
    if LIGHT.is_active:
        return "light is on"
    return "light is off"


@app.route('/light/blink')
def light_blink():
    _blink(5)


@app.route('/static/<path>')
def static_html(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


@app.route('/form/simple', methods=['POST'])
def simple():
    return "You submitted simple"

@app.route('/form/form', methods=['POST'])
def show_values():
    first = request.form['first_name']
    last = request.form['last']
    gender = request.form['gender']
    return "{} {} is a {}.".format(first, last, gender)


@app.route('/form/form2', methods=['POST'])
def show_values2():
    first = request.form['first']
    last = request.form['last']
    gender = request.form['gender']
    return render_template('form_reply.html', first = first, last = last, gender = gender)


@app.route('/form/blink', methods=['POST'])
def form_blink():
    bad_input = "We only deal with positive integers"
    
    try:
        num_times_to_blink = int(request.form['n_blink'])
    except ValueError:
        return bad_input
    
    # Checking for a positive integer greater than 0
    if num_times_to_blink < 1:
        return bad_input
    
    _blink(num_times_to_blink)
    return "Done blinking"

 
if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
