address =input()
address = address.split(":")
# ''은 전체 길이가 8이 될때까지 0000으로 채우기.

for idx,val in enumerate(address):
    if val == '':
        while len(address) < 8 :
            address.insert(idx,'0000')
        address[idx] = '0000'
    else:
        while len(address[idx]) < 4:
            address[idx] = '0' + address[idx]

address = ':'.join(address)
while len(address) > 39:
    address = address.replace('0000:0000','0000')

print(address)