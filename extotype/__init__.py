from os import path
from sphinx.jinja2glue import SphinxFileSystemLoader
from sphinx.application import Sphinx
from docutils import nodes
from hashlib import md5
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from json import dumps
from pathlib import Path

data = {}

def xyz(app, exception):
    if app.builder.name != 'text':
        return
    print(app.outdir)
    for p in Path(app.outdir).glob('**/*.txt'):
        absolute_path = p.as_posix()
        relative_path = absolute_path.replace(app.outdir, '')
        with open(absolute_path, 'r') as f:
            content = f.read()
        data[relative_path] = {
            'checksum': md5(content.encode('utf-8')).hexdigest()
        }
    print(dumps(data, indent=2))

# def generate_embeddings(app, doctree, docname):
#     print(doctree.astext())
#     data[docname] = {}
#     for section in doctree.traverse(nodes.section):
#         text = section.astext()
#         text = text.replace('\n', ' ')
#         checksum = md5(text.encode('utf-8')).hexdigest()
#         data[docname][checksum] = text

def add_static_dir(app):
    if app.builder.name != 'html':
        return
    extension_dir = path.dirname(path.abspath(__file__))
    static_dir = path.join(extension_dir, 'static')
    app.builder.config.html_static_path.append(static_dir)
    template_dir = path.join(extension_dir, 'templates')
    app.builder.templates.pathchain.insert(1, template_dir)
    app.builder.templates.loaders.insert(1, SphinxFileSystemLoader(template_dir))
    app.builder.templates.templatepathlen += 1

# def generate_index(app, exception):
#     if app.builder.name != 'text':
#         return
#     documents = SimpleDirectoryReader(app.outdir).load_data()
#     index = GPTSimpleVectorIndex.from_documents(documents)
#     index.save_to_disk(path.join(app.outdir, 'index.json'))

def setup(app):
    app.connect('builder-inited', add_static_dir)
    # app.connect('doctree-resolved', generate_embeddings)
    # app.connect('build-finished', generate_index)
    app.connect('build-finished', xyz)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
