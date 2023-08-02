"""'Must specify access token via Authorization header. https://developer.github.com/changes/2020-02-10-deprecating-auth-through-query-param' hatası çözümü hakkında
ve Sadık Turan'ın api uygulama dersi kodu
"""

import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "########################################" # <== Token buraya yazılacak
        self.headers = {"Authorization": "token "+self.token} # Token'ı headers olarak göndermemiz gerekiyormuş. 
    def getUser(self,userName):
        response = requests.get(self.api_url+"/users/"+ userName)
        return response.json()

    def getRepo(self, userName):
        repoRes = requests.get(self.api_url +"/users/" + userName +"/repos")
        jsonResRepo = repoRes.json()
        for repo in jsonResRepo:
            print(repo["name"])
    
    def newRepo(self, name):
        repoRes = requests.post(self.api_url +"/user/repos", headers=self.headers, json={
            "name": name,
            "description":"This is first repo that is created with python",
            "homepage":"https://github.com",
            "private":False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki":True
        })
        return repoRes.json()
github = Github()

while True:
    choice = input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\nChoice: ")
    if choice == '4':
        break
    else:
        if choice == '1':
            username = input("Username: ")
            result = github.getUser(username)
            print(f"Name: {result['name']} Public Repos:{result['public_repos']} Followers: {result['followers']}")
        elif choice == '2':
            username = input("Username: ")
            github.getRepo(username)
        elif choice == '3':
            repoName = input("Repository name: ")
            result = github.newRepo(repoName)
            print(result)
        else:
            print("Invalid Input")
