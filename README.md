# extotype

A repository for prototyping Sphinx extensions.

## Deploying

```
# python3 -m venv sandbox
source ~/Sandbox/sandbox/bin/activate
# python3 -m pip install setuptools wheel twine
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

### ~/.pypirc

```
[pypi]
username = <TODO>
password = <TODO>
```

### Notes

* https://www.sphinx-doc.org/en/master/development/theming.html#distribute-your-theme-as-a-python-package
