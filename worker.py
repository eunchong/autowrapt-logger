from random import random
from time import sleep

# -----------------------

def ll1lIIll1ll1lI():
    sleep(random()*0.1)

def ll11IIll1ll1lI():
    sleep(random()*0.2)

def ll11IIll1ll1l1():
    sleep(random()*0.4)

def ll1lIIllIll1lI():
    sleep(random()*0.5)

def ll11IIll1llllI():
    sleep(random()*0.8)

# -----------------------

def get_db_data():
    ll1lIIllIll1lI()
    ll1lIIll1ll1lI()

def get_redis_data():
    ll1lIIll1ll1lI()
    ll1lIIll1ll1lI()

def logic_a():
    ll11IIll1ll1lI()
    ll1lIIll1ll1lI()

def logic_b():
    ll11IIll1ll1l1()
    ll1lIIll1ll1lI()

def logic_c():
    ll11IIll1llllI()
    ll11IIll1ll1lI()

# -----------------------

def job():
    get_db_data()
    get_redis_data()
    logic_a()
    logic_b()
    logic_c()

def run():
    for i in range(10000):
        print('job: %d'%i)
        job()
