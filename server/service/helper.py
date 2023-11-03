def create_dict(data_values, column_names):
    data_dict = dict()
    for i in range(len(column_names)):
        if column_names[i] == 'created_on':
            date = str(data_values[i])
            data_dict[column_names[i]] = date
        else:
            data_dict[column_names[i]] = data_values[i]
    return data_dict


def split_dict(dict):
    key = dict.keys()
    values = dict.values()
    return [key, values]
