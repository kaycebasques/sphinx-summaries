import json
import hashlib

import docutils

data = {}

def generate_summary(app, doctree, docname):
    for section in doctree.traverse(docutils.nodes.section):
        text = section.astext()
        hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        data[docname] = {'hash': hash}

def dump(app, exception):
    print(json.dumps(data, indent=4))

def setup(app):
    app.connect('doctree-resolved', generate_summary)
    app.connect('build-finished', dump)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
