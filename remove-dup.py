from collections import OrderedDict
def dup(s):
    return "".join(OrderedDict.fromkeys(s))
if __name__ == "__main__":
    s=str(input())
    print(dup(s))
