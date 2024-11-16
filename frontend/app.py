from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = "secret-key"

# Temporary storage for answers
answers = {"state": "", "position": ""}

# Sample profiles for matching
profiles = [
    {"name": "Alice", "job": "Software Engineer", "image": "https://via.placeholder.com/300x400"},
    {"name": "Bob", "job": "Data Scientist", "image": "https://via.placeholder.com/300x400"},
    {"name": "Charlie", "job": "Product Manager", "image": "https://via.placeholder.com/300x400"},
]

matches = []


@app.route('/')
def home():
    return render_template('intro.html', profiles=profiles)


@app.route('/submit', methods=['POST'])
def submit():
    global answers
    data = request.json
    answers["state"] = data.get("state")
    answers["position"] = data.get("position")
    return jsonify({"message": "Answers saved"}), 200


@app.route('/matching', methods=['POST'])
def matching():
    if request.method == 'POST':
        profile = request.json
        matches.append(profile)
        return jsonify({"message": "Added to matches"}), 200
    return render_template('matching.html', profiles=profiles)


if __name__ == '__main__':
    app.run(debug=True)
