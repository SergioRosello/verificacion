init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run code/concatenate.py
	coverage report -m