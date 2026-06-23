from flask import Flask, render_template, abort
from flask_frozen import Freezer
# pyrefly: ignore [missing-import]
from flask_flatpages import FlatPages
import os

app = Flask(__name__)

# --- Configuration ---
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True

app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'content'

pages = FlatPages(app)
freezer = Freezer(app)

# --- Dynamic Routes ---
@app.route('/')
def index_root():
    return render_template('index_es.html', current_page='index', lang='es')

@app.route('/<lang>/')
def index(lang):
    if lang not in ['es', 'en']:
        abort(404)
    return render_template(f'index_{lang}.html', current_page='index', lang=lang)

@app.route('/<lang>/<page>/')
def render_page(lang, page):
    if lang not in ['es', 'en']:
        abort(404)
    template_name = f'{page}_{lang}.html'
    if not os.path.exists(os.path.join(app.root_path, 'templates', template_name)):
        abort(404)
    return render_template(template_name, current_page=page, lang=lang)

# --- Blog Routes ---
@app.route('/<lang>/blog/')
def blog_list(lang):
    if lang not in ['es', 'en']:
        abort(404)
    # Get all pages and filter by language
    articles = [p for p in pages if p.meta.get('lang') == lang and p.meta.get('category')]
    # Sort them by date
    articles.sort(key=lambda item: item.meta.get('date', ''), reverse=True)
    return render_template('blog.html', current_page='blog', lang=lang, articles=articles)

def has_category(page, category_name):
    cat = page.meta.get('category')
    if not cat:
        return False
    if isinstance(cat, list):
        return any(str(c).strip().lower() == category_name.strip().lower() for c in cat)
    return str(cat).strip().lower() == category_name.strip().lower()

@app.route('/<lang>/blog/category/<category>/')
def blog_category(lang, category):
    if lang not in ['es', 'en']:
        abort(404)
    articles = [p for p in pages if p.meta.get('lang') == lang and has_category(p, category)]
    articles.sort(key=lambda item: item.meta.get('date', ''), reverse=True)
    return render_template('blog.html', current_page='blog', lang=lang, articles=articles, selected_category=category.title())

@app.route('/<lang>/blog/<path:path>/')
def blog_post(lang, path):
    post = pages.get_or_404(path)
    if post.meta.get('lang') != lang:
        abort(404)
    return render_template('post.html', current_page='blog', lang=lang, post=post)

if __name__ == '__main__':
    app.run(debug=True)
