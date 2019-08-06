from collections import OrderedDict
def dup(ss):
    return "".join(OrderedDict.fromkeys(ss))
if __name__ == "__main__":
    ss=str(input())
    print(dup(ss))
