conda:
	conda env create --file environment.yml

requirements:
	pip install -r app/requirements.txt

fetch:
	cd app; python fetch_data.py --credentials api-credentials.json users mechatronics3d
