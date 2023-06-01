"""
GROUP_NAME = dossa_d

MEMBERS =
	dossa_d
	qasmi_m
	gueye_d
"""
import json
import sys


def minimum_classrooms(file_path: str) -> int:
    """
    Calculate minimum number of classesrooms needed for a day.

    Parameters
    ----------
    file_path : str
        Path to the file with the daily classroom sessions.

    Returns
    -------
    None.
    """
    classrooms = 0

    with open(file_path, 'r') as f:
        sessions = f.read()
        sessions = json.loads(sessions)

        for index in range(len(sessions)):
            session = sessions[index]
            simultaneous_sessions = 0
            precedent_sessions = sessions[:index]

            if not precedent_sessions:
                classrooms += 1
                continue

            for precedently in precedent_sessions:
                if session['start'] >= precedently['start'] and session['start'] < precedently['end']:
                    simultaneous_sessions += 1

            if simultaneous_sessions >= classrooms:
                classrooms += 1

        return classrooms


if len(sys.argv) >= 2:
    try:
        classes = minimum_classrooms(sys.argv[1])
        print(classes)
    except Exception as e:
        print('Error: File not found or not a valid JSON file.\n')
else:
    print('Error: Try again with a file path as an argument.\n')
