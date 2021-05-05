import json
import requests
import ipfsapi
api = ipfsapi.Client('127.0.0.1', 5001)


with open('json/list_ipfs.json') as f:
  data = json.load(f)

print(data[0])

pinataBaseURL= "https://api.pinata.cloud/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI1NDMwMzE3YS1lYjIxLTQzOWQtOTFhOS01NGI1MjZjNTExNmUiLCJlbWFpbCI6InU1MTEuNTExLjUxMXVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZX0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImI3MmE1M2MzY2YyOTcwY2RlYjk5Iiwic2NvcGVkS2V5U2VjcmV0IjoiYmUxNTY2ODYxNjg2MjY0MzQzNWYyOGUwMjlhZTVjZmU5MWQ0ZWRlM2ZmMjY1MjQ1ODExNGMzZDQ0N2FjYjQxMSIsImlhdCI6MTYxOTk3MTM4N30.lkwJ6aHx9ByF7uXLVkFIKeHe9mf7DBlrapK_4fYh1JQ/pin"
#(put your personal pinata api key here)
headers = {'pinata_api_key': 'b72a53c3cf2970cdeb99' ,
'pinata_secret_api_key': 'be15668616862643435f28e029ae5cfe91d4ede3ff2652458114c3d447acb411'} #(put your personal pinata secret api key here)

headers2 = {'Authorization':'Bearer yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI1NDMwMzE3YS1lYjIxLTQzOWQtOTFhOS01NGI1MjZjNTExNmUiLCJlbWFpbCI6InU1MTEuNTExLjUxMXVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZX0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImYzMjhhNTViNWVjODRjZjZlNTFiIiwic2NvcGVkS2V5U2VjcmV0IjoiMDMzM2EzYmY1MzQ4ZDkwYWJmNjM5MjM3MzJmOGJmNTg5ZWMxNDQ0MTVmNTY5NGRhN2E0MWFjNGYzNWE3YzEwOCIsImlhdCI6MTYyMDIwMTQ1Mn0.5ZDCNaiV1OvP3XdDgpz3dVQ3aqGO49YlYJhXDjTha_4' } #(put your personal pinata secret api key here)


pinFile = "https://api.pinata.cloud/psa/pins"

print(type(headers))


for i in range(len(data)):
    pin={
    "cid": data[i]["Hash"],
    "name": data[i]["Name"]
    }



    r = requests.post(url=pinFile , json = pin, headers= headers2)

    print(r.status_code)



