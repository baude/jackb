from flask import Flask, render_template
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

@app.route('/light/blink/<number>')
def light_blink(number)
    LIGHT.blink(on_time=1, off_time=1, n= ('number'))

        
    
    
    

if __name__ == '__main__':
   app.run()
