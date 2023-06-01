"""
GROUP = gueye_d 1005565

MEMBERS = 
	dossa_d
	qasmi_m
	gueye_d
"""
import json
import sys


def benefits_prediction(buildings):
    """
    Calculates the annual benefits of the rent based on the orientation of the apartment.

    Parameters
    ----------
    buildings : list
        List of buildings oriented on the west-east axis

    Returns
    -------
    benefits : int.
    """
    benefits = 0
    current_max_height = 0

    for building in reversed(buildings):
        height = building['height']
        floor_layout = building['floor_layout']

        relevant_floors = (
            floor for floor in floor_layout
            if 'E' in floor['orientations'] and
            height > current_max_height
        )

        for floor in relevant_floors:
            monthly_benefits = round(floor['monthly_rent'] * 0.05 + 0.49)
            year_benefits = monthly_benefits * \
                12 * (height - current_max_height)
            benefits += year_benefits

        current_max_height = max(current_max_height, height)

    return benefits


if len(sys.argv) >= 2:
    try:
        buildings = json.loads(sys.argv[1])
        benefits = benefits_prediction(buildings)
        print(benefits)
    except:
        print("try again with correct json format!")
else:
    print("try with some data in json table format (list of numbers)")
