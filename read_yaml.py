import yaml
list=[]
with open('test1.yaml','r',encoding='utf-8') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    for i in data.values():
        list.append((i.get('name'),i.get('age')))
    print(list)