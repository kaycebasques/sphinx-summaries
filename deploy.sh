# python3 -m venv sandbox
source ~/Sandbox/sandbox/bin/activate
# python3 -m pip install setuptools wheel twine
python3 setup.py sdist bdist_wheel
twine upload dist/*
deactivate
