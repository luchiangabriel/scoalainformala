from utils import print_header
from extending_mutable_sequence import crayons_box

print_header('__len__')
print(len(crayons_box))

print_header('__getitem__')
print(crayons_box[2])

print_header('__contains__')
if 'Blue' in crayons_box:
    print('Blue crayon is in the crayon box')

print_header('__iter__')
for crayon in crayons_box:
    print(crayon)

print_header('__delitem__')
print(crayons_box.__delitem__(0))

print_header('__setitem__')
print(crayons_box.__setitem__(0, 'Orange'))

print_header('insert')
print(crayons_box.insert(0, 'Purple'))
