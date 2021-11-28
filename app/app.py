import argparse
import datetime
import pickle
import pipe
import json

from thai_strftime import thai_strftime
from api import LINENotifyAPI

now = datetime.date.today()

def main(path_pkl, path_config):
    pickle_in = pickle.load(open(path_pkl, "rb"))
    config = json.load(open(path_config,"r",encoding="utf-8"))
    result = list((pickle_in | pipe.where(lambda x: x["date"] == "2021-01-06")))

    if len(result) > 0:
        # Format data
        data = datetime.datetime.strptime(result[0]["date"], "%Y-%m-%d").date()

        text = config["line"]["message"].format(
            date=thai_strftime(data, "%d %B %Y"),
            type="แรม" if result[0]["type"] == 0 else "ขึ้น",
            type_num=result[0]["type_num"],
            month=result[0]["month"],
            year=result[0]["year"]
        )

        # Send message LINE Notify API
        response = LINENotifyAPI(config["line"]["token"]).send(text)

        if response.status_code == 200:
            print("[%s] Message sent successfully." % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            print("[%s} Message sent failed. [%s] %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), response.status_code, response.text))

parser = argparse.ArgumentParser(description='LINE Notify Bud Alert arguments.')
parser.add_argument(
    'bud',
    metavar='--bud', 
    type=str, 
    nargs='?',
    default='mond.pkl',
    help='Path mond file'
)
parser.add_argument(
    'config',
    metavar='--config', 
    type=str, 
    nargs='?',
    default="config.json",
    help='Path config.json file'
)

args = parser.parse_args()
main(args.bud, args.config)