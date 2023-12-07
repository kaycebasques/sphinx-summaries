import json
import hashlib

import docutils
import transformers

summarizer = transformers.pipeline('summarization', model='google/pegasus-xsum')
data = {}

def generate_summary(app, doctree, docname):
    text = doctree.astext()
    hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    summary = summarizer(text)['summary_text']
    data[docname] = {
        'hash': hash,
        'summary': summary
    }

def dump(app, exception):
    print(json.dumps(data, indent=4))

def setup(app):
    app.connect('doctree-resolved', generate_summary)
    app.connect('build-finished', dump)
    return {
        'version': '0.0.3',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
