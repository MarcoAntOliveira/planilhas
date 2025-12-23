all:
	python3 treino.py
	rm -rf treino.pdf
	typst compile treino.typ 