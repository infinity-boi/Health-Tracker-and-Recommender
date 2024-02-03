import json


def lines_list(filename, access, pair, search_key1=None, search_key2=None):
    file = open(filename, access)
    json_data = json.load(file)
    if pair == "kv":
        keys = []
        values = []
        for key in json_data.keys():
            keys.append(key)
            values.append(json_data[key])
        return [keys, values]
    elif pair == "k":
        keys = []
        for key in json_data.keys():
            keys.append(key)
        return keys
    elif pair == "v":
        values = []
        for key in json_data.keys():
            values.append(json_data[key])
        return values
    elif pair == "vk":
        for key in json_data.keys():
            if key == search_key1:
                value = json_data[key]
                keys = list(value.keys())
                return keys
    elif pair == "vv":
        for key in json_data.keys():
            if key == search_key1:
                value = json_data[key]
                for value_key in value.keys():
                    if value_key == search_key2:
                        value_value = list(value[value_key])
                        return value_value
    else:
        file.close()
        return


