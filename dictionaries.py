dic1={1:10,2:20,3:30}
dic2={4:40,5:50,6:60}
dic3={7:70,8:80}
dic4={ }
for d in(dic1,dic2,dic3):
    dic4.update(d)
    print(dic4)