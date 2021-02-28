import json
import os
os.chdir('../Testdata/json/')
f=open("signup.json","r")
f1=open("signin.json",'r')

def getdata():
    loaded_json = json.load(f)
    # print(loaded_json)
    signupdata=[]
    for x in loaded_json:
        # x['Email'])
        signupdata.append(x['Email'])
        signupdata.append(x['Phone'])
    # for x in loaded_json:
# 	print("%s: %d" % (x, loaded_json[x]))

    return signupdata

# print(getdata())

def getdata_signin():
    loaded_json = json.load(f1)
    # print(loaded_json)
    signindata=[]
    for x in loaded_json:
        # x['Email'])
        signindata.append(x['username'])
        signindata.append(x['password'])
    # for x in loaded_json:
# 	print("%s: %d" % (x, loaded_json[x]))
#     f1.close()
    return signindata

# print(getdata_signin())