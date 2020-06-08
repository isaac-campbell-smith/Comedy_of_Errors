from flask import Flask, render_template, request, jsonify
import os

POSTER_FOLDER = os.path.join('static', 'images/one')

app = Flask(__name__)
app.config['IMAGES'] = POSTER_FOLDER

@app.route('/', methods=['GET'])
def index():
    posters = sorted([os.path.join(app.config['IMAGES'], img) for img in os.listdir(POSTER_FOLDER) if img.endswith('.jpg')])
    return render_template('recommender.html', user_images = posters)

@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    one = user_data['one']
    two = user_data['two']
    three = user_data['three']
    four = user_data['four']
    five = user_data['five']
    six = user_data['six']
    seven = user_data['seven']
    eight = user_data['eight']
    nine = user_data['nine']
    ten = user_data['ten']
    recommendations = _recommend(one, two, three, four, five, six, seven, eight, nine, ten)
    return jsonify({'recommendations':recommendations})

def _recommend(one, two, three, four, five, six, seven, eight, nine, ten):
    if one:
        print (posters[0])
        recommendations = posters[0]
    return recommendations

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)