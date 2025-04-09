run:
	python alien_invasion.py

test:
	pytest

build:
	pyinstaller --onefile alien_invasion.py --name alien_invasion

clean:
	rm -rf __pycache__ build dist alien_invasion.spec
