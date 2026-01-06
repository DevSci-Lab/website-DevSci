from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# --- Route Configuration ---
# Rules:
# 1. Map URL to the correct language template (*_es.html or *_en.html).
# 2. Pass 'current_page' (base name) and 'lang' ('es' or 'en') to render_template.
# 3. Maintain legacy URL support where possible by mapping them to the ES version.

@app.route('/')
def index():
    return render_template('index_es.html', current_page='index', lang='es')

@app.route('/index_es.html')
def index_es():
    return render_template('index_es.html', current_page='index', lang='es')

@app.route('/index_en.html')
def index_en():
    return render_template('index_en.html', current_page='index', lang='en')

# --- Researchers / Investigadores ---
@app.route('/researchers_es.html')
@app.route('/investigadores.html') # Legacy support
def researchers_es():
    return render_template('researchers_es.html', current_page='researchers', lang='es')

@app.route('/researchers_en.html')
@app.route('/researchers.html') # Legacy support
def researchers_en():
    return render_template('researchers_en.html', current_page='researchers', lang='en')

# --- Students / Alumnado ---
@app.route('/students_es.html')
@app.route('/alumnado.html') # Legacy support
def students_es():
    return render_template('students_es.html', current_page='students', lang='es')

@app.route('/students_en.html')
@app.route('/students.html') # Legacy support
def students_en():
    return render_template('students_en.html', current_page='students', lang='en')

# --- Contact ---
@app.route('/contact_es.html')
@app.route('/contact.html') # Default to ES for generic contact URL
def contact_es():
    return render_template('contact_es.html', current_page='contact', lang='es')

@app.route('/contact_en.html')
def contact_en():
    return render_template('contact_en.html', current_page='contact', lang='en')

# --- Generic ---
@app.route('/generic_es.html')
@app.route('/generic.html') # Legacy
def generic_es():
    return render_template('generic_es.html', current_page='generic', lang='es')

@app.route('/generic_en.html')
def generic_en():
    return render_template('generic_en.html', current_page='generic', lang='en')

# --- Elements ---
@app.route('/elements_es.html')
@app.route('/elements.html') # Legacy
def elements_es():
    return render_template('elements_es.html', current_page='elements', lang='es')

@app.route('/elements_en.html')
def elements_en():
    return render_template('elements_en.html', current_page='elements', lang='en')

if __name__ == '__main__':
    app.run(debug=True)
