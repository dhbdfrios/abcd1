import yaml
data = {'name': 'lisi', 'age': 11, 'weight': 22.2, 'isclass': True, 'data': None, 'date': '2018/02/17'}
with open('test4.yaml','w',encoding='utf-8') as f:
    yaml.dump(data,f)
