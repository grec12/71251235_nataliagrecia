def palindrom(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrom(s[1:-1])
    else:
        return False
    
kalimat = input("Masukkan kalimat: ")
if palindrom(kalimat):
    print("Kalimat tersebut adalah palindrom.")
else:
    print("Kalimat tersebut bukan palindrom.")

    