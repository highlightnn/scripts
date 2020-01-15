CONFIG1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
print (list(CONFIG1.split()[-1].split(',')))