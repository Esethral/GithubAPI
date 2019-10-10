import requests
import json

def getRequest(user, int):
    URL = "https://api.github.com/users/"+user+"/repos"
    r = requests.get(URL)
    repo = json.loads(r.text)
    if (int < len(repo)):
        repo = json.loads(r.text)[int]['name']
        URL = "https://api.github.com/repos/"+user+"/"+repo+"/commits"
        r = requests.get(URL)
        commits = json.loads(r.text)
        return 'Repo: ' + repo + " || Commits: " + str(len(commits)) + "\n" + getRequest(user, int+1)
    return ""

print(getRequest("esethral", 0))
