def dict_to_list(d):
    result = []
    for key in d:
        result.append([key, d[key]])
    return result

d=input()
print(dict_to_list(d))