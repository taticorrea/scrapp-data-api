install-requirements:
	pip install -r requirements.txt

scrapp-data:
	python3 data/poc_prezunic
	python3 data/poc_mercadolivre

up-api:
	uvicorn main:app --reload	

get-api:
	python3 get.py >> response.txt

post-api:
	python3 post.py
