source venv/bin/activate
python3 setup.py sdist bdist_wheel
twine upload dist/*
deactivate
