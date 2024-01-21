def translate(d):
    s = ''
    for i in d:
        if i not in ('rasrsa'):
            s += i + "o" + i
        else:
            s += i 
    print(s)
    
translate("zugzug")
