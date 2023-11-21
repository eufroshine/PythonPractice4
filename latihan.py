#list
list = [1, 2, 3, 4, 5]

#print element 3
print("Element ke 3")
print(list[2])

#element 2 sampai 4
print("Element ke 2 sampai 4")
a = list[1:4]
print(a)

#element akhir
print("Element Akhir")
akhir = list[-1]
print (akhir)

#change element 4 
print("Merubah Element ke 4")
list[3]=7
print(list)

#change element 4 to end
print("Merubah Element ke 4 sampai akhir")
list[3:5] = [6, 7,]
print (list)

#list b
print("List b")
mirror_list = list[0:2]
print(mirror_list)

#adding string
print("Menambahkanb string")
mirror_list.append("test")
print(mirror_list)

#adding 3 element
print("Menambahkan 3 Element")
mirror_list.extend([4, 5, 6])
print(mirror_list)

#adding list a + b
print("Menambahkan List a dengan List b")
print(list + mirror_list)
