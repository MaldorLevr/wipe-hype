import json

config_file = json.load(open('settings.json'))

rust_log_path = '{}\RustClient_Data\output_log.txt'.format(config_file['rustPath'])
server_ip = config_file['serverIp']
