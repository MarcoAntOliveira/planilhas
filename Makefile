all:train
	

train:
	python3 treino.py
	sleep 5
	@clear
	rm -rf treino.pdf
	typst compile treino.typ 
	@xdg-open treino.pdf

 train2:
	python3 treino2.py
	sleep 5
	@clear
	rm -rf treino.pdf
	typst compile treino.typ 
	@xdg-open treino.pdf