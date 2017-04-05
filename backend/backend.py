from flask import Flask, render_template, session, request
from gpiozero import LED

app = Flask(__name__)

LIGHT = LED(17)

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
    LIGHT.blink(on_time=1, off_time=1, n=5)


@app.route('/static/<path>')
def static_html(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


@app.route('/form/simple', methods=['POST'])
def simple():
    return "You submitted simple"

@app.route('/form/form', methods=['POST'])
def show_values():
    first = request.form['first']
    last = request.form['last']
    gender = request.form['gender']
    return "{} {} is a {}.".format(first, last, gender)


@app.route('/form/form2', methods=['POST'])
def show_values2():
    first = request.form['first']
    last = request.form['last']
    gender = request.form['gender']
    return render_template('form_reply.html', first = first, last = last, gender = gender)
  
if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
