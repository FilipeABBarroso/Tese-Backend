import json  
import requests

def getSitemap(entity):
  url = f"https://web-check.xyz/api/sitemap?url={entity}"

  response = requests.get(url)
  save_file = open("outputs/savedata-sitemap.json", "w")  
  json.dump(json.loads(response.text), save_file, indent = 6)  
  save_file.close()  
  print("Done!")