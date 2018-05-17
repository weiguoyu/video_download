clean: clear_pyc

clear_pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

server-install:
	pip install -r requirements.txt

server: server-install
	#todo

clean-env:
	pip freeze | xargs pip uninstall -y

dev-install:
	pip install -r dev_requirements.txt

dev-start:
    #todo
