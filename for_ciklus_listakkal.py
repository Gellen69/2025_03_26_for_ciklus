# f string
gyumolcsok = ["apple", "banana", "cherry"]
for gyumolcs in gyumolcsok:
#   print(gyumolcs + " gyumolcsok")
  print(f"lista adott gyumolcse: {gyumolcs}......")

# listahoz elem hozzaadasa (python add list element)
gyumolcsok.append("mango")
# print(gyumolcsok)

if "apple" in gyumolcsok:
    gyumolcsok.remove("apple")
else:
   gyumolcsok.append("apple")

print(gyumolcsok)

