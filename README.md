# Mobile Data Management Project

This is a Django project to manage mobile data, including information about mobile models, country producers, nationalities, prices, colors, sizes, and availability status.

## Features

1. Save Mobile Data: Add new mobile models with related information to the database.
2. Forms: Use simple templates to store mobile data with validation.
3. Reports: Retrieve data in JSON format based on specific criteria.
4. Unpredicted Data and Functions: Additional functionality for future use.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`
3. Create the database and perform migrations by running: `python manage.py makemigrations` and `python manage.py migrate`
4. Run the development server with: `python manage.py runserver`

## Usage

1. Save Mobile Data:
   - Access the form to add new mobile models and their details by visiting `http://localhost:8000/add/`

2. Reports:
   - Get a list of all mobiles with nationality "korea": `http://localhost:8000/report/korea_nationality/`
   - Get a list of mobiles with the same brand name (provide brand_name in POST data): `http://localhost:8000/report/brand_mobiles/`
   - Get a list of mobiles with the same country producer and nationality: `http://localhost:8000/report/same_country_nationality/`

