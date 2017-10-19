import random,time
def fnc():
    s=""
    x=random.randint(0,100)
    for i in range(x):
        s=s+"#"
    s=s+"\n"
    return s
while True:
    print fnc()
    time.sleep(0.2)
