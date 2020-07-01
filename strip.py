with open('yjh_base64.txt','r') as file:
	data = file.read()
	data_pure = data.replace('\n','')

with open('yjh_pure.txt','w') as f:
	f.write(data_pure)