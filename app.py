from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# --- Configuration ---
# Generate clean URLs (directories with index.html) for static build
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True

# --- Routes ---
# We use specific function names (e.g., index_es, contact_en) because base.html
# relies on them for logic like url_for(current_page + '_' + lang).
# The URLs are mapped to be "clean" (no .html extension).
# IMPORTANT: Trailing slashes are required for Frozen-Flask to generate folders (e.g. /contact/index.html)

@app.route('/')
def index():
    # Redirect root to ES version or render directly
    return render_template('index_es.html', current_page='index', lang='es')

@app.route('/es/')
def index_es():
    return render_template('index_es.html', current_page='index', lang='es')

@app.route('/en/')
def index_en():
    return render_template('index_en.html', current_page='index', lang='en')

# --- Researchers ---
@app.route('/researchers/')
def researchers_es():
    return render_template('researchers_es.html', current_page='researchers', lang='es')

@app.route('/researchers-en/')
def researchers_en():
    return render_template('researchers_en.html', current_page='researchers', lang='en')

# --- Students ---
@app.route('/students/')
def students_es():
    return render_template('students_es.html', current_page='students', lang='es')

@app.route('/students-en/')
def students_en():
    return render_template('students_en.html', current_page='students', lang='en')

# --- Contact ---
@app.route('/contact/')
def contact_es():
    return render_template('contact_es.html', current_page='contact', lang='es')

@app.route('/contact-en/')
def contact_en():
    return render_template('contact_en.html', current_page='contact', lang='en')

# --- Generic ---
@app.route('/generic/')
def generic_es():
    return render_template('generic_es.html', current_page='generic', lang='es')

@app.route('/generic-en/')
def generic_en():
    return render_template('generic_en.html', current_page='generic', lang='en')

# --- Elements ---
@app.route('/elements/')
def elements_es():
    return render_template('elements_es.html', current_page='elements', lang='es')

@app.route('/elements-en/')
def elements_en():
    return render_template('elements_en.html', current_page='elements', lang='en')

if __name__ == '__main__':
    app.run(debug=True)
