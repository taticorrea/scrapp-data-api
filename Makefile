install-requirements:
	python3 -m pip install -r requirements.txt

extract-data:
	python3 data/extract.py

transform-data:	
	python3 data/transform.py

extract-transform-data:
	python3 data/extract.py
	python3 data/transform.py	

up-api:
	uvicorn api.main:app --reload

load-data-api:
	python3 data/load.py

get-data-api:
	python3 data/get.py

delete-data-api:
	python3 data/delete.py