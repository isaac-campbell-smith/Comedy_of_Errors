from browser import document, ajax, console
import json
def get_inputs(event):
  #print (document.value)
  print ('FOO_BAR')
  ''' special_one = document['one'].click
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
          'ten': int(special_ten)}
  '''
  return 'FOO_BAR'

def display_solutions(req):
  result = json.loads(req.text)
  document['recommendations'].html = f"{result['recommendations']}"

def send_inputs_json(inputs):
  req = ajax.Ajax()
  req.bind('complete', display_solutions)
  req.open('POST',
              '/solve',
              True)
  req.set_header('Content-Type', 'application/json')
  req.send(json.dumps(inputs))

def click1(event):
  send_inputs_json(1)

def click2(event):
  send_inputs_json(2)

def click3(event):
  send_inputs_json(3)

def click4(event):
  send_inputs_json(4)

def click5(event):
  send_inputs_json(5)

def click6(event):
  send_inputs_json(6)

def click7(event):
  send_inputs_json(7)

def click8(event):
  send_inputs_json(8)

def click9(event):
  send_inputs_json(9)

def click10(event):
  send_inputs_json(10)

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