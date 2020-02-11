
ip = '192.163.3.1'
ip = ip.split('.')
a, b, c, d = tuple(ip)
a = int(ip[0])
b = int(ip[1])
c = int(ip[2])
d = int(ip[3])
result_table = '''
    {:<10} {:<10} {:<10} {:<10}
    {:010b} {:010b} {:010b} {:010b}
    '''
print(result_table.format(a, b, c, d, a, b, c, d))
