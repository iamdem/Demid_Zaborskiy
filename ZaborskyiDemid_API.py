import requests
import json

url = ["https://content.dropboxapi.com/2/files/upload",
       "https://api.dropboxapi.com/2/sharing/get_file_metadata",
       "https://api.dropboxapi.com/2/files/delete_v2"]

payload = {}
headers = {
    'Dropbox-API-Arg': '{"path": "/My_Random_File.txt","mode": "add","autorename":'
                       ' true,"mute": false,"strict_conflict": false}',
    'Content-Type': 'application/octet-stream',
    'Authorization': 'Bearer HWTfQ7T4BTUAAAAAAAAAAbGxMmzxUTzM_D7S-Aoa6sACjR7A-5CnAhVPGES3icJ1'
}

response = requests.request("POST", url[0], headers=headers, data=payload)
print(response.text)

file_id = json.loads(response.text)['id']
payload = json.dumps({
  "file": f"{file_id}",
  "actions": []
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer HWTfQ7T4BTUAAAAAAAAAAbGxMmzxUTzM_D7S-Aoa6sACjR7A-5CnAhVPGES3icJ1'
}

response = requests.request("POST", url[1], headers=headers, data=payload)
print(response.text)

payload = json.dumps({
  "path": "/My_Random_File.txt"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer HWTfQ7T4BTUAAAAAAAAAAbGxMmzxUTzM_D7S-Aoa6sACjR7A-5CnAhVPGES3icJ1'
}

response = requests.request("POST", url[2], headers=headers, data=payload)
print(response.text)
