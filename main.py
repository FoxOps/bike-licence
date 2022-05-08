import datetime
import jinja2
import json
import bl_functions


data: dict = json.load(open(data.json))
age: int = time_passed(data['date_of_birth'])
years_permis_a2: int = time_passed(data['date_permis_a2'])
