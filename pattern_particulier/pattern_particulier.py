"""
GROUP = dossa_d 994386

MEMBERS =
	dossa_d
	qasmi_m
	gueye_d
"""
import json
import re
import sys


def search_pattern(pattern: str, file_path: str) -> list:
    """
    Searches a pattern in a file and returns the results.

    Parameters
    ----------
    pattern: str
            The pattern to search.
    file_path: str
        The path of the file to search in.

    Returns
    -------
    list
        The results of the search.
    """
    results = {}
    with open(file_path, 'r') as f:
        text = f.read()

    gathering = [gathered.start() for gathered in re.finditer(pattern, text)]
    return map(lambda gathered: {
        'file': file_path,
        'pattern': pattern,
        'offset': gathered,
    },  gathering)


if len(sys.argv) >= 2:
    try:
        if '-e' in sys.argv:
            patterns = [
                pattern for pattern in sys.argv
                if sys.argv.index(pattern) > 1 and
                sys.argv[sys.argv.index(pattern) - 1] == '-e'
            ]
            files = [
                file for file in sys.argv
                if sys.argv.index(file) > 1 and
                sys.argv[sys.argv.index(file) - 1] != '-e' and file != '-e'
            ]
        gathered = []
        for file in files:
            for pattern in patterns:
                gathered += search_pattern(pattern, file)

        gathered = json.dumps(gathered)
        print(gathered)
    except Exception as e:
        print('Error: File not found or not a valid JSON file.\n')
else:
    print('Error: Try again with a file path as an argument.\n')
