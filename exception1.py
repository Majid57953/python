try:
    print(int('a'))
except ValueError as exp:
    print(exp.args)