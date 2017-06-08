import re
content = """\
50172961,"THERAVANCE INC","901 جينوا ب ينوا بوليفار س ينوا باوث فرنسوليفار س ينوا بوليفار سيسكو كالاوث فرنس ينوا بوليفار سيفورنيا 94064A;سكو كالاوث فرنس ينوا ب򀙈ليفار سيفورنيا 94064A;سكو كالاوث فرنس򀙈ليفار سيفورنيا 94064A;سكو كالاوث فرنس򀙊فورنيا 94064A;سكو كالاوث فرنس򀙊فورنيا 94064A;سكو كال򀙊فورنيا 94080","US","",9,33431,"THERAVANCE INC",27623584,"THERAVANCE",1,"COMPANY",3531336,"THERAVANCE INC",2
"""
try:
    with open(r'reg_only_alphanum.txt', 'r', encoding='utf-8') as f:
        l = f.read()
        print(l)
        new_l = re.sub("[^a-zA-Z0-9#!,\"[\u0627-\u064a]]+", " ", str(l))
        print(new_l)
except:
    print(content)
    new_l = re.sub("[^a-zA-Z0-9#!,\"[\u0627-\u064a]]+", " ", str(content))
    print(new_l)
print(l==new_l)
