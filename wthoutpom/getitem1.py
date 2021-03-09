class ABC:
    Dealsicon = '//i[@class="money icon"]'
    Companiesicon = '//i[@class="building icon"]'
    Taskicon = '//i[@class="tasks icon"]'
    iconlist = [Companiesicon, Taskicon,Dealsicon]

    # def __getitem__(self, item):
    #     return self.iconlist[item]

a=ABC()
icon="Dealsicon"
j=0
# for i in a.iconlist:
#     if "money" in i:
#         print(i)

print(getattr(a,icon))