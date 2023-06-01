"""
GROUP_NAME = dossa_d

MEMBERS = 
	dossa_d
	qasmi_m
	gueye_d
"""
import json
import sys


def bourse_predictor(predictions: list) -> list:
    """
    Use predictions to calculate the ideal time to buy / sell a bourse product.
    We will calculate the complexity of the function using : complexity(predictions_length) where predictions_length is the number of predictions

    Parameters
    ----------
    predictions : list
        list of numbers representing the predicted price of a bourse product.

    Returns
    -------
    best_dates: List
        List of the indexes corresponding to the best moments for buying/selling the product
    """
    indexes = []
    buying = True

    try:
        if predictions[0] < predictions[1]:
            indexes.append(0)
            buying = False

        for index in range(1, len(predictions) - 1):
            if (
                buying and
                predictions[index - 1] >= predictions[index] and
                predictions[index] < predictions[index + 1]
            ) or \
                (
                not buying and
                predictions[index - 1] < predictions[index] and
                predictions[index] >= predictions[index + 1]
            ):
                indexes.append(index)
                buying = not buying

        if not buying and predictions[-1] > predictions[-2]:
            indexes.append(len(predictions) - 1)

        if len(indexes) % 2 != 0:
            indexes.pop()

        return indexes
    except Exception as e:
        pass


if len(sys.argv) >= 2:
    try:
        predictions = json.loads(sys.argv[1])
        best_dates = bourse_predictor(predictions)

        best_dates = json.dumps(
            best_dates) if best_dates is not None else json.dumps([])

        print(best_dates)
    except Exception as e:
        print(e)
else:
    print("try with some data in json table format (list of numbers) \n")
