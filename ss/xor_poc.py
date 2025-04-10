c1 = list(')":#?4kQXG\\1lVRl9$48')
c2 = list('zdAWWQ4394mR3943akfE')
p = ""
for i in range(len(c1)):
    p += chr(ord(c1[i]) ^ ord(c2[i]))

print(p)