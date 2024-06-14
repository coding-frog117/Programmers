import sys
N = int(input())
ip_address = []
for i in range(N):
    inp = list(input().split('.'))
    ip = []
    for idx,v in enumerate(inp):
        ip.append(inp[idx])
    ip_address.append(ip)

network_address = ip_address[0]
subnet_mask = 33
for add_idx,address in enumerate(ip_address):
    for idx,v in enumerate(address):
        result = format(int(network_address[idx]) ^ int(v),'b')
        if result != '0':
            subnet_mask = min(subnet_mask,(8 - len(result)) + (8*idx))
            break

for idx,v in enumerate(network_address):
    network_address[idx] = format(int(v),'b')
    while len(network_address[idx]) < 8:
        network_address[idx] = '0'+network_address[idx]
network_address = ''.join(network_address)[:subnet_mask]
network_mask = '1'*subnet_mask

while len(network_address) < 32:
    network_address += '0'
    network_mask += '0'
network_address_arr =[]
network_mask_arr = []

s = 0
e = 8
while e <= 32:
    network_address_arr.append(str(int(network_address[s:e],2)))
    network_mask_arr.append(str(int(network_mask[s:e],2)))
    s += 8
    e += 8

print('.'.join(network_address_arr))
print('.'.join(network_mask_arr))