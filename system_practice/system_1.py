# f=open("hello.txt","w+")
# for i in range(10):
# 	f.write("Hello World!!\n")
# f=open("hello.txt","a+")
# for i in range(10):
# 	f.write("monkey group\n")
# f=open("hello.txt", "r")
# if f.mode=='r':
# 	contents=f.read()
# 	print(contents)
# f.close()

# f=123456789
# f=open("hello.txt","w+")
# f.write('123456789')
# f.seek(4)
# print(f.read(1))

import pickle
favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "hello.txt", "wb" ) )
portfolio=[{'name':'IBM','shares':56,'price':23}, {'name':'Dell','shares':9.8,'price':30}, {'name':'HP','shares':6.6,'price':3.2}, {'name':'Apple','shares':9.6,'price':2.3}, {'name':'Microsoft','shares':5.6,'price':13}]
