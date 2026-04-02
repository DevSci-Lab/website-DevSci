import os
import re

tpl_dir = 'templates'
for fname in os.listdir(tpl_dir):
    if not fname.endswith('.html'):
        continue
        
    path = os.path.join(tpl_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace url_for('index_' + lang) -> url_for('index', lang=lang)
    content = content.replace("url_for('index_' + lang)", "url_for('index', lang=lang)")
    
    # In index_es/index_en specifically, current_page is 'index', so url_for(current_page + '_es') -> url_for('index', lang='es')
    if fname in ['index_es.html', 'index_en.html']:
        content = content.replace("url_for(current_page + '_es')", "url_for('index', lang='es')")
        content = content.replace("url_for(current_page + '_en')", "url_for('index', lang='en')")
        content = content.replace("url_for('index')", "url_for('index_root')")
        
    # Other hardcoded page + lang
    for p in ['researchers', 'students', 'contact']:
        content = content.replace(f"url_for('{p}_' + lang)", f"url_for('render_page', page='{p}', lang=lang)")
        content = content.replace(f"url_for('{p}_es')", f"url_for('render_page', page='{p}', lang='es')")
        content = content.replace(f"url_for('{p}_en')", f"url_for('render_page', page='{p}', lang='en')")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed URLs.")
