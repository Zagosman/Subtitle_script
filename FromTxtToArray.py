with open('new 1.txt',encoding="utf8") as file:
    txt = file.read()
    txtArray = txt.split('\n\n')

print(txtArray)
print(len(txtArray))
print('Hello, world!')

with open('export.txt','w', encoding='windows-1251') as file:
    file.write(repr(txtArray))