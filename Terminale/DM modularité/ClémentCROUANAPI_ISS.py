from re import M
import requests as r

def peopleSpace():
    """renvoie le nom de toutes les personnes dans l espace"""
    rep = r.get('http://api.open-notify.org/astros.json')
    l = []
    n = len(rep.json()['people'])
    for i in range(n):
        l.append(rep.json()['people'][i]['name'])
    return l

def ISSPosition():
    """renvoie la position de l iss"""
    rep = r.get('http://api.open-notify.org/iss-now.json')
    l = rep.json()
    #timestamp correspond a la seconde a laquelle la position a etee recuperee (nombre de secondes ecoulees depuis le 1er janvier 1970 UTC)
    return l['iss_position']
