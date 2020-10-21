import yaml
from yaml import load, load_all

stream = open('C:\\Users\\pkinane\\Documents\\DevNetAsc_200-901\\my_code\\cbt_nuggets\\cbt_nuggets\\parsing_files\\yamlsample.yml')
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))


