install-requirements:
	python3 -m pip install -r requirements.txt

scrapp-data:
	python3 data/webscrapping.py

up-api:
	uvicorn api.main:app --reload

get-api:
	python3 get.py > response.txt

post-api:
	python3 post.py

delete-api:
	python3 delete.py