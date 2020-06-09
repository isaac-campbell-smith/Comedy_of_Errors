from browser import bind, document, ajax, console
from browser.widgets.dialog import InfoDialog
import json

def display_solutions(req):
  result = json.loads(req.text)
  document['special_title'].html = result['special_title']
  document['recommendations_1'].html = result['recommendations_1']
  document['recommendations_2'].html = result['recommendations_2']
  document['recommendations_3'].html = result['recommendations_3']
  document['results'].style.display = "inline"

def send_inputs_json(inputs):
  req = ajax.Ajax()
  req.bind('complete', display_solutions)
  req.open('POST',
              '/solve',
              True)
  req.set_header('Content-Type', 'application/json')
  req.send(json.dumps(inputs))

def results(inputs):
  send_inputs_json(inputs)
  # if display == "none" else "none"

def bigClick(event):
  selection = document['all_special'].value
  send_inputs_json(selection)

def click1(event):
  results(1)

def click2(event):
  results(2)

def click3(event):
  results(3)

def click4(event):
  results(4)

def click5(event):
  results(5)

def click6(event):
  results(6)

def click7(event):
  results(7)

def click8(event):
  results(8)

def click9(event):
  results(9)

def click10(event):
  results(10)

document['1'].bind('click', click1)
document['2'].bind('click', click2)
document['3'].bind('click', click3)
document['4'].bind('click', click4)
document['5'].bind('click', click5)
document['6'].bind('click', click6)
document['7'].bind('click', click7)
document['8'].bind('click', click8)
document['9'].bind('click', click9)
document['10'].bind('click', click10)
document['all_special_button'].bind('click', bigClick)
