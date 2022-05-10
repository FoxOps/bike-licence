###############################################################################
#
# Bonjour !
# Je suis un test.
#
################################################################################

from flask import request
import bl_functions


def bike_licence_info():
    data: dict = request.json()
    age: int = bl_functions.time_passed(data['date_of_birth'])
    error_dict: dict = {}
    permis_list: list = []
    years_permis_a2: int = bl_functions.time_passed(data['date_permis_a2'])

    if age < 0 or years_permis_a2 < 0:
        error_dict = {
            "title": "Erreur !",
            "text": "Les dates ne peuvent être dans le future."
            }

    if age >= 14:
        permis_list.append(bl_functions.info_permis_am())

    if age >= 16 and data["permis_b"] is False:
        permis_list.append(bl_functions.info_permis_a1())
    elif age >= 16 and data["permis_b"] is True:
        permis_list.append(bl_functions.info_permis_a1_7heures())

    if age >= 18:
        permis_list.append(bl_functions.info_permis_a2())
    if age >= 20 and data["permis_a2"] is True:
        permis_list.append(bl_functions.info_permis_a())

    return permis_list, error_dict
