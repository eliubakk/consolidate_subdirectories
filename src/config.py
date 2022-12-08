import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'Source': "'/'",
                     'Dest': "'/'"}

with open('example.ini', 'w') as configfile:
  config.write(configfile)