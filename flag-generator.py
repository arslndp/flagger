#!/usr/bin/python3
from random import choice
from string import *
import sched , time , datetime
path_soal = ['player/arsalan/bof',
             'player/arsalan/ldap',
             'player/arsalan/rop',
             'player/hayra/bof',
             'player/hayra/ldap',
             'player/hayra/rop']

interval = 10
print("[!] memulai")
s = sched.scheduler(time.time , time.sleep)

def generate(len_flag , num_flag):
    plain = ascii_uppercase + ascii_lowercase + str(digits)
    #print("[+] plain : " + plain)

    flag = ["".join([choice(plain) for i in range(len_flag)]) for j in range(num_flag)]
    for i in range(len(flag)):
        return "HackFest{" + flag[i] + "}"

def send_flag(path,flag):
    #for i in range(len(path)):
    write = open(path , "w")
    write.write(str(flag))
    write.close()
    print("[+] sukses kirim flag ke " + path)
    print("[+] flag : " + str(flag))

def main(sc):
    now = datetime.datetime.now()
    print("[+] preparing ")
    print("[+] flag di ubah ")
    print("[+] perubahan : " + str(now))
    len_flag = 25
    num_flag = len(path_soal)
    for i in range(num_flag):
        flag = generate(len_flag , 1)
        send = send_flag(path_soal[i] + "/flag.txt" , flag)
        print("==============================")
    s.enter(5 , 1 , main, (sc,))

if __name__ == '__main__':
    s.enter(interval , 1 , main, (s,))
    s.run()
