def list_from_dict(id, dictionary):
    if id in dictionary.keys():
        return id, dictionary[id]
    else:
        return id,"no id"

def main():
    lst = ["ABCD", "LMN" , "STU" , "PQRS" ]
    dic = { 'ABCD':'kajal' , 'LMN' :'John' , 'PQRS' : 'Anni'}

    for items in lst:
        print(list_from_dict(items,dic))

if __name__ == "__main__":
    print("begin-------")
    main()