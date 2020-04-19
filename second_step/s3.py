import re

def fetch(contents):
    pat = re.compile(r'/v1/'+r'(.*?)(\?|\/|$)')
    pMatch = re.search(pat,contents)
    return pMatch.group(1)


print(fetch("/v1/fruits?name=1"))
print(fetch("/v1/fruits/1"))
print(fetch("/v1/fruits"))


