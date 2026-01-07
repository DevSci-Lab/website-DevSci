from app import app, freezer
import os

if __name__ == '__main__':
    freezer.freeze()

    cname_path = os.path.join('docs', 'CNAME')
    with open(cname_path, 'w') as f:
        f.write('devscilab.com')
