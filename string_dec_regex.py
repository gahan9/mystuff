import re


s = 'a9*a9 + a10*a10 + a8*a8 + a255*a255 + b58*b58 + c58*c58'
string = re.sub('[ ]', '', s)  # removed whitespace from string (optional:only if you are not sure how many space you can get in string)
x = string.split('+')
pattern = re.compile(r'([a-z])([\d]+)')
ans = ''
for element in x:
    for letter, num in re.findall(pattern, element):
        st = ''
        for i in range(len(element.split('*'))):
            st = st + '*' + (letter+str(int(num)-i))
            # print(str(letter) + str(int(num)-i))
    ans = ans + '+' + st[1:]
print(ans[1:])
