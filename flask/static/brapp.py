from browser import document, ajax, console
import json
def get_inputs():
  special_one = document['one'].click
  special_two = document['two'].value
  special_three = document['three'].value
  special_four = document['four'].value
  special_five = document['five'].value
  special_six = document['six'].value
  special_seven = document['seven'].value
  special_eight = document['eight'].value
  special_nine = document['nine'].value
  special_ten = document['ten'].value
  return {'one': int(special_one),
          'two': int(special_two),
          'three': int(special_three),
          'four': int(special_four),
          'five': int(special_five), 
          'six': int(special_six),
          'seven': int(special_seven),
          'eight': int(special_eight),
          'nine': int(special_nine),
          'ten' int(special_ten)}

def display_solutions(req):
  result = json.loads(req.text)
  document['solution'].html = f"{result['recommendations']}"
    #xxxdocument['solution'].html = 'foo'

def send_inputs_json(inputs):
  req = ajax.Ajax()
  req.bind('complete', display_solutions)
  req.open('POST',
              '/solve',
              True)
  req.set_header('Content-Type', 'application/json')
  req.send(json.dumps(inputs))

def click(event):
  inputs = get_inputs()
  send_inputs_json(inputs)

document['solve'].bind('click', click)