init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run code/textAnalizer.py
	coverage report -m