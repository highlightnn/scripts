ospf_route = "O                      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
route = ospf_route.split()
a, a1 = ['Protocol:', route[0].replace('O', 'OSPF')]
b, b1 = ['Prefix:',route[1]]
c, c1 = ['AD/Metric:',route[2].strip('[]')]
d, d1 = ['Next-Hop:',route[4].strip(',')]
e, e1 = ['Last update:',route[5].strip(',')]
f, f1 = ['Outbound Interface:',route[6]]
result_table = '''
    {:24} {:24}
    {:24} {:24}
    {:24} {:24}
    {:24} {:24}
    {:24} {:24}
    {:24} {:24}
    '''
print(result_table.format(a, a1, b, b1, c, c1, d, d1, e, e1, f, f1))
