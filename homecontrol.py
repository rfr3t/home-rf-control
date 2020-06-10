import rflib
from bottle import route, run, abort
import devices.rfdevices as rf

d=rflib.RfCat()

@route('/fireplace/<action>')
def control_fireplace(action):
    if action == 'on':
        rf.Fireplace().turnon(d)
    elif action == 'off':
        rf.Fireplace().turnoff(d)
    else:
        abort(404, "Not Found")
    return "ok"

@route('/bedroom-2-light/<action>')
def control_light(action):
    if action == 'on':
        rf.Bedroom2FanLight().turn_light_on(d)
    elif action == "off":
        rf.Bedroom2FanLight().turn_light_off(d)
    else:
        abort(404, "Not Found")
    return "ok"

@route('/bedroom-2-fan/<action>')
def control_fan(action):
    if action == 'off':
        rf.Bedroom2FanLight().turn_fan_off(d)
    elif action == 'low':
        rf.Bedroom2FanLight().set_fan_low(d)
    elif action == 'med':
        rf.Bedroom2FanLight().set_fan_medium(d)
    elif action == 'high':
        rf.Bedroom2FanLight().set_fan_high(d)
    else: 
        abort(404, "Not Found")
    return "ok"

@route('/bedroom-1-light/<action>')
def control_light(action):
    if action == 'on':
        rf.Bedroom1FanLight().turn_light_on(d)
    elif action == "off":
        rf.Bedroom1FanLight().turn_light_off(d)
    else:
        abort(404, "Not Found")
    return "ok"

@route('/bedroom-1-fan/<action>')
def control_fan(action):
    if action == 'off':
        rf.Bedroom1FanLight().turn_fan_off(d)
    elif action == 'low':
        rf.Bedroom1FanLight().set_fan_low(d)
    elif action == 'med':
        rf.Bedroom1FanLight().set_fan_medium(d)
    elif action == 'high':
        rf.Bedroom1FanLight().set_fan_high(d)
    else: 
        abort(404, "Not Found")
    return "ok"

@route('/livingroom-fan/<action>')
def control_fan(action):
    if action == 'low':
        rf.LivingRoomFan().set_fan_low(d)
    else:
        abort(404, "Not Found")
    return "ok"

run(host='0.0.0.0', port=80)
