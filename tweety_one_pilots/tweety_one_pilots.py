"""
GROUP = gueye_d 1005565

MEMBERS =
	dossa_d
	qasmi_m
	gueye_d
"""
import json
import sys


def most_used_hashtags(file_path: str) -> None:
    """
    Returns the most used hashtags of twitter from a list of hashtags inside a file.

    Parameters
    ----------
    file_path : str
        Path to the file containing the tweets.
    Returns
    -------
    hashtags : str(dict).
    """
    hashtags = []
    with open(file_path, 'r') as f:
        tweets = json.loads(f.read())
        for tweet in tweets['tweets']:
            hashtags += tweet['hashtags']

        hashtags = list(map(
            lambda hashtag:
                (hashtags.count(hashtag) * 100 / len(hashtags), hashtag),
            hashtags
        ))
        hashtags.sort(key=lambda hashtag: hashtag[1])
        hashtags = filter(
            lambda hashtag: hashtag[0] >= tweets['percentage_threshold'],
            hashtags
        )
        hashtags = list(map(lambda hashtag: hashtag[1], hashtags))
        hashtags = list(dict.fromkeys(hashtags))
        hashtags = json.dumps(hashtags)

        return hashtags


if len(sys.argv) >= 2:
    try:
        print(most_used_hashtags(sys.argv[1]))
    except Exception as e:
        print('Error: File not found or not a valid JSON file.\n')
else:
    print('Error: Try again with a file path as an argument.\n')
