Dealsicon = (By,'//i[@class="money icon"]')
Companiesicon = '//i[@class="building icon"]'
Taskicon = '//i[@class="tasks icon"]'

licon=[Companiesicon, Taskicon,Dealsicon]

icon="money"
icon1=""
for i in licon:
    if icon in i:
        icon1=i

print(icon1)

