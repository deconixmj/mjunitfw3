import json
import os
os.chdir('D:\Py_projects\mjunitfw3_testsuite_nose\Testdata\json')
f=open("signup.json","r")
f1=open("signin.json","r")
f2=open("contacts.json","r")

def getdata_signup():
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
    signindata=[]
    for x in loaded_json:
        # x['Email'])
        signindata.append(x['username'])
        signindata.append(x['password'])
    #     f1.close()
    return signindata

# print(getdata_signin())

def getcontacts_data():

    loaded_json=json.load(f2)
    contacts_data=[]
    for x in loaded_json:
        cdata=[]
        cdata.append(x['first_name'])
        cdata.append(x['last_name'])
        cdata.append(x['company'])

        contacts_data.append(cdata)

    return contacts_data

# print(getcontacts_data())

