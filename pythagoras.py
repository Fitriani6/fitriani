print("login sederhana")
print("---------------")
my_username = input("buat username baru anda :")
my_password = input("buat passwoard baru anda :")
print("-----------DATA DIKONFIRMASI------------")

your_username = input("masukan username anda :")
your_password = input("masukan pin anda :")

if my_username==your_username and my_password==your_password:
    print("------------------------------------------------")
    print("login berhasil,welcome" + my_username + "..")
    print("------------------------------------------------")
else:
   print("-------------------------------------------------") 
   print("login gagal,silahkan coba lagi...")
   print("-------------------------------------------------")




print("menghitung rumus segitiga pythagora")
print("-----------------------------------")

print("mencari sisi miring")
print("-------------------")
sisi_alas = float(input("masukan nilai sisi alas :"))
sisi_tegak = float(input("masukan nilai sisi tegak :"))

sisi_miring = (sisi_alas **2 + sisi_tegak **2) **(0.5)
print(f"apabila sisi alas (sisi alas) dan sisi tegak(sisi_tegak) maka sisi miring adalah :", sisi_miring)

print("mencari sisi tegak")
print("------------------")
sisi_alas = float(input("masukan nilai sisi alas :"))
sisi_miring = float(input("masukan nilai sisi miring :"))

sisi_tegak = (sisi_miring **2 - sisi_alas **2) **(0.5)
print(f"apabila sisi miring (sisi miring) dan sisi alas(sisi_alas) maka sisi tegak adalah :", sisi_tegak)

print("mencari sisi alas")
print("-----------------")
sisi_miring = float(input("masukan nilai sisi miring :"))
sisi_tegak = float(input("masukan nilai sisi tegak :"))

sisi_alas = (sisi_miring **2 - sisi_tegak **2) **(0.5)
print(f"apabila sisi miring (sisi miring) dan sisi tegak(sisi_tegak) maka sisi alas adalah :", sisi_alas)

