from point import point

def processpoint():
    userlist=[]
    user_file=open('point.txt','r')
    for i in user_file:
        list=i.split(',')
        s=point(list[0],list[1])
        userlist.append(s)
    return userlist

