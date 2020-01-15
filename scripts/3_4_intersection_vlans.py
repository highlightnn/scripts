CONFIG1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
CONFIG2 = "switchport trunk allowed vlan 1,3,100,200,300"
vlan1 = set((CONFIG1.split())[-1].split(','))
vlan2 = set((CONFIG2.split())[-1].split(','))
vlans = vlan1.intersection(vlan2)
vlans = list(vlans)
vlans = [int(i) for i in vlans]
vlans.sort()
print(vlans)