from app import app, freezer, pages
import os

@freezer.register_generator
def index():
    for lang in ['es', 'en']:
        yield {'lang': lang}

@freezer.register_generator
def render_page():
    templates_dir = os.path.join(app.root_path, 'templates')
    for t in os.listdir(templates_dir):
        if t.endswith('_es.html') and not t.startswith('index'):
            yield {'lang': 'es', 'page': t.replace('_es.html', '')}
        elif t.endswith('_en.html') and not t.startswith('index'):
            yield {'lang': 'en', 'page': t.replace('_en.html', '')}

@freezer.register_generator
def blog_list():
    for lang in ['es', 'en']:
        yield {'lang': lang}

@freezer.register_generator
def blog_category():
    categories = {}
    for p in pages:
        lang = p.meta.get('lang')
        cat = p.meta.get('category')
        if lang and cat:
            if isinstance(cat, list):
                for c in cat:
                    categories.setdefault(lang, set()).add(str(c).strip().lower())
            else:
                categories.setdefault(lang, set()).add(str(cat).strip().lower())
            
    for lang, cats in categories.items():
        for cat in cats:
            yield {'lang': lang, 'category': cat}

@freezer.register_generator
def blog_post():
    for p in pages:
        lang = p.meta.get('lang')
        if lang:
            yield {'lang': lang, 'path': p.path}

if __name__ == '__main__':
    freezer.freeze()

    cname_path = os.path.join('docs', 'CNAME')
    with open(cname_path, 'w') as f:
        f.write('devscilab.com')
