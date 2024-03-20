install-requirements:
	python3 -m pip install -r requirements.txt

extract-data:
	python3 data/extract.py

transform-data:	
	python3 transform.py

up-api:
	uvicorn api.main:app --reload

load-data-api:
	python3 load.py

get-data-api:
	python3 get.py > response.txt

delete-data-api:
	python3 delete.py