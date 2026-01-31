mn={"a": 1, "b": 2}
def reverse_dict(mn):
    reversed_mn = {}
    for key, value in mn.items():
        reversed_mn[value] = key
    print(reversed_mn)
reverse_dict(mn)