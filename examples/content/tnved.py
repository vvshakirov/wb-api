import os

from dotenv import load_dotenv

from wb_api import WBApi

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
tnveds = content.get_tnved(subject_ID=1)

for tnved in tnveds:
    print(tnved.tnved)
    print(tnved.is_kiz)
