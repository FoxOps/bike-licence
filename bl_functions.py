from datetime import date, datetime


def time_passed(input_str: str) -> int:
    input_date = datetime.strptime(input_str, '%d/%m/%Y')
    today = date.today()
    year_passed: int = today.year - input_date.year - \
        ((today.month, today.day) < (input_date.month, input_date.day))

    return year_passed


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
        'bike_pic': 'https://btcmotors.fr/15202-tm_thickbox_default/'
                    'masai-greystone-50cc.jpg'
    }

    return permis_am


def info_permis_a1() -> dict:
    permis_a1 = {
        'name': 'Permis A1',
        'info': 'Pour les personnes souhaitant conduire une motocyclette dont '
                'la cylindrée n’excède pas 125 cm3, dont la puissance n’excède'
                ' pas 11 kW et dont le rapport puissance/poids est inférieur à'
                ' 0,1 kW par kilogramme.',
        'bike_exemple': 'Zero DS',
        'bike_pic': 'https://d29sx7s964xey6.cloudfront.net/a70df09a-2264-45a8'
                    '-a92d-a496e6c317cb_DS+14.4+360+alpha_0102.png?auto=compr'
                    'ess,format&w=1920&h=1080&fit=clamp'
    }

    return permis_a1


def info_permis_a1_7heures() -> dict:
    permis_a1_7heures = {
        'name': 'Permis A1 - Formation de 7 heures',
        'info': 'Les personnes titulaires du permis B qui souhaitent conduire '
                'un deux-roues motorisé de 50 à 125 cm3 peuvent obtenir la '
                'catégorie A1 du permis de conduite grâce à une équivalence : '
                '\"la formation de 7 heures\"',
        'bike_exemple': 'Zero DS',
        'bike_pic': 'https://d29sx7s964xey6.cloudfront.net/a70df09a-2264-45a8'
                    '-a92d-a496e6c317cb_DS+14.4+360+alpha_0102.png?auto=compr'
                    'ess,format&w=1920&h=1080&fit=clamp'
    }

    return permis_a1_7heures


def info_permis_a2() -> dict:
    permis_a2 = {
        'name': 'Permis A2',
        'info': 'Pour les personnes souhaitant conduire une moto d’une '
                'puissance n’excédant pas 35 kW ; dont le rapport puissance'
                '/poids est inférieur à 0,2 kW/kg et qui n\'est pas issue '
                'd\'un modèle développant plus de 70 kW.',
        'bike_exemple': 'Indian scout bobber',
        'bike_pic': 'https://cdn1.polaris.com/globalassets/indian/2022/model/'
                    'vehicle-cards/indian-scout-bobber-black-metallic.png?v='
                    'a22db7a3&format=webp'
    }

    return permis_a2


def info_permis_a() -> dict:
    permis_a = {
        'name': 'Permis A',
        'info': 'La catégorie A du permis de conduire permet la conduite de '
                'toutes les motocyclettes et tricycles ainsi que les '
                'quadricycles à moteur d’une puissance maximum de 15 kW. Un '
                'titulaire d’un permis A2 depuis plus de 2 ans peut se voir '
                'délivrer, après une formation de 7h, un permis de la '
                'catégorie A.',
        'bike_exemple': 'Kawasaki Ninja H2R',
        'bike_pic': 'https://storage.kawasaki.eu/public/kawasaki.eu/en-EU/'
                    'model/19ZX1000Y_201GY3DRS1CG_A.png'
    }

    return permis_a
