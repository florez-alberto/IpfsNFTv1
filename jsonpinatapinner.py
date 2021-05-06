import json
import requests
import ipfsapi

with open('json/list_ipfs.json') as f:
  data = json.load(f)



headers2 = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI1NDMwMzE3YS1lYjIxLTQzOWQtOTFhOS01NGI1MjZjNTExNmUiLCJlbWFpbCI6InU1MTEuNTExLjUxMXVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZX0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjVlOTRhNDE0ZDNjZTEzN2QzMTA4Iiwic2NvcGVkS2V5U2VjcmV0IjoiZmU3N2EzZGMxYjc3ZDBlYmZhZTU3NGE2YjFkMWZkMDE0NmUwODBlMjhjOTk2NGQ5ZDk1NTEwZjA0ZGRkMDJkZiIsImlhdCI6MTYyMDMwMDg1Mn0.stwXmrz08WjAV44tM9IYohOhSCRXzQlGQA37WWuxHGw' } #(put your personal pinata secret api key here)
pinFile = "https://api.pinata.cloud/psa/pins"



for i in range(len(data)):
    pin={
    "cid": data[i]["Hash"],
    "name": data[i]["Name"]
    }



    r = requests.post(url=pinFile , json = pin, headers= headers2)

    print(r.status_code)

