import requests
import sys

def check(userid):
    resCheck = requests.get('https://discord.riverside.rocks/check.json.php?id=' + userid)
    return resCheck.json()

def report(userid, token, reason):
    resCheck = requests.get('https://discord.riverside.rocks/report.json.php?key=' + token + '&id=' + userid + '&details=' + reason)
    return resCheck.json()
