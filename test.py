from dotenv import load_dotenv
load_dotenv()
import os
import pprint

curDir = os.getcwd()

token=os.environ.get('api-token')
print(token)
print(os.environ['VALPY-KEY'])