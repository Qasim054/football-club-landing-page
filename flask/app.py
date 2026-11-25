from flask import Flask, render_template

app = Flask(__name__)

# Squad Data (No Images, Pure Stats & Roles)
squad_data = [
    {"no": "01", "name": "Tayyab", "position": "Goalkeeper", "role": "GK", "age": 24, "status": "Fit", "apps": 18, "clean_sheets": 9},
    {"no": "04", "name": "Alwaz", "position": "Center-Back", "role": "DEF", "age": 22, "status": "Fit","Captain" "apps": 20, "goals": 2},
    {"no": "05", "name": "Sameer", "position": "Left-Back", "role": "DEF", "age": 22, "status": "Fit", "apps": 17, "goals": 1},
    {"no": "05", "name": "Ahad", "position": "Right-Back", "role": "DEF", "age": 22, "status": "Fit", "apps": 17, "goals": 1},
    {"no": "10", "name": "Qasim", "position": "Central Midfielder", "role": "MID", "age": 21, "status": "apps", "apps": 21, "goals": 18},
    {"no": "08", "name": "Hadi", "position": "Attacking Mid", "role": "MID", "age": 21, "status": "Fit", "apps": 19, "goals": 5},
    {"no": "11", "name": "Bakar", "position": "Striker", "role": "FWD", "age": 21, "status": "Fit", "apps": 21, "goals": 14},
   
]

# Fixtures Data
fixtures_data = [
    {"opponent": "Kotli Strikers", "competition": "AJK Premier League", "date": "28 NOV 2026", "time": "16:00 PKT", "venue": "Quaid-e-Azam Stadium", "type": "HOME", "result": "UPCOMING"},
    {"opponent": "Bhimber FC", "competition": "AJK Premier League", "date": "05 DEC 2026", "time": "15:30 PKT", "venue": "Bhimber Sports Complex", "type": "AWAY", "result": "UPCOMING"},
    {"opponent": "Muzaffarabad Titans", "competition": "Kashmir Cup", "date": "18 NOV 2026", "time": "16:00 PKT", "venue": "Quaid-e-Azam Stadium", "type": "HOME", "result": "W 3 - 1"},
    {"opponent": "Poonch Warriors", "competition": "AJK Premier League", "date": "10 NOV 2026", "time": "15:00 PKT", "venue": "Rawalakot Ground", "type": "AWAY", "result": "D 1 - 1"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/squad')
def squad():
    return render_template('squad.html', players=squad_data)

@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html', matches=fixtures_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
