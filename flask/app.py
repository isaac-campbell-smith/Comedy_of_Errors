from flask import Flask, render_template, request, jsonify
import pickle
import os

with open ('RECS.pkl', 'rb') as f:
    RECS = pickle.load(f)

MENU_KEYS = {}
for k, v in RECS.items():
    MENU_KEYS[v[0]] = k

POSTER_KEYS = {
                1: [40],
                2: [245],
                3: [100],
                4: [78],
                5: [39],
                6: [128],
                7: [73],
                8: [143],
                9: [186],
                10: [76]
                }

POSTER_FOLDER = os.path.join('static', 'images/one')
app = Flask(__name__)
app.config['IMAGES'] = POSTER_FOLDER

@app.route('/', methods=['GET'])
def index():
    posters = sorted([os.path.join(app.config['IMAGES'], img) for img in os.listdir(POSTER_FOLDER) if img.endswith('.jpg')])
    return render_template('recommender.html', user_images = posters)

@app.route('/solve', methods=['POST'])
def solve():
    btn_key = request.json
    if type(btn_key) == int:
        special = RECS[POSTER_KEYS[btn_key][0]]
    else:
        special = RECS[MENU_KEYS[btn_key]]
    special_title = special[0]
    love, meh, hate = ",  ".join(special[1]), ",  ".join(special[2]), ",  ".join(special[3])
    return jsonify({'special_title':special_title, 'recommendations_1':love, 'recommendations_2':meh, 'recommendations_3':hate})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)