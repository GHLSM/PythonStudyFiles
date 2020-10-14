import random
def v_code():
    ret=''
    for i in range(5):
        num=random.randint(0,9)
        cha=chr(random.randint(65,122))
        s=str(random.choice([num,cha]))
        ret+=s
    return ret
print(v_code())

