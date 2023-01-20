import configparser

def write_ini():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45'}
    config['jarvis'] = {}
    config['jarvis']['User'] = 'johnny'
    config['jarvis']['botname'] = 'shiela'
    with open('example.ini', 'w') as configfile:
        config.write(configfile)