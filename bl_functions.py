from datetime import date, datetime


def time_passed(input_str):
    input_date = datetime.strptime(input_str, '%d/%m/%Y')
    today = date.today()
    age = today.year - input_date.year - \
        ((today.month, today.day) < (input_date.month, input_date.day))

    return age


def info_permis_am() -> dict:
    permis_am = {
        'name': 'Permis AM',
        'info': 'La catégorie AM permet de conduire dès 14 ans des '
                'cyclomoteurs (motocyclettes de moins de 50 cm3) et des '
                'voiturettes (quadricycles légers). Elle est délivrée à '
                'l’issue d’une formation d’une durée minimale de 8 heures. '
                'Cette catégorie est la seule exclue du régime de permis à '
                'points.',
        'bike_exemple': 'Masai Greystone 50',
        'bike_pic': ''
    }

    return permis_am


def info_permis_a1() -> dict:
    permis_a1 = {
        'name': 'Permis A1',
        'info': 'hsdflkjdklfjsldkfjksdflkjsdf',
        'bike_exemple': 'Masai Greystone 50',
        'bike_pic': ''
    }

    return permis_a1


def info_permis_a1_7heures() -> dict:
    permis_a1_7heures = {
        'name': 'Permis A1 - Formation de 7 heures',
        'info': 'La catégorie AM permet de conduire dès 14 ans des ',
        'bike_exemple': 'Masai Greystone 50',
        'bike_pic': ''
    }

    return permis_a1_7heures


def info_permis_a2() -> dict:
    permis_a2 = {
        'name': 'Permis A2',
        'info': 'hsdflkjdklfjsldkfjksdflkjsdf',
        'bike_exemple': 'Masai Greystone 50',
        'bike_pic': ''
    }

    return permis_a2


def info_permis_a() -> dict:
    permis_a = {
        'name': 'Permis A',
        'info': 'hsdflkjdklfjsldkfjksdflkjsdf',
        'bike_exemple': 'Masai Greystone 50',
        'bike_pic': ''
    }

    return permis_a
