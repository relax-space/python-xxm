import re

def fetch(contents):
    pat = re.compile(r'/v1/'+r'(.*?)(\?|\/|$)')
    pMatch = re.search(pat,contents)
    return pMatch.group(1)


print(fetch("/v1/fruits?name=1"))
print(fetch("/v1/fruits/1"))
print(fetch("/v1/fruits"))


print("===="*20)


def fetch2(contents):
    pat = re.compile(r'(^|\?|\&)name='+r'(.*?)(&|$)')
    pMatch = re.search(pat,contents)
    return pMatch.group(2)


print(fetch2("name=xxm"))
print(fetch2("/v1/fruits?name=lm"))
print(fetch2("/v1/fruits?name=ldeh&age=2"))
print(fetch2("/v1/fruits?sex=1&name=zyx"))
print(fetch2("/v1/fruits?sex=1&name=gfc&age=2"))
