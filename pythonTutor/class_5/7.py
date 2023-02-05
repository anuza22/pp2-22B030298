#«Удаление фрагмента»
a = input()
k = a.find("h")
k1 = a.rfind("h")

a = a.replace(a[k:k1+1], "")
print(a)
