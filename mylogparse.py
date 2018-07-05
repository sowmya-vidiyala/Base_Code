List = []
Check_list = []
Temp = []
List_new = []
v = ''
with open('cat logfile.txt', 'r') as file:
    x = file.read()
    List = x.split("\n")
    for i in range(1, len(List)):
        x = List[i]
        Temp = x.split("    ")
        Temp.remove(Temp[2])
        v = "    ".join(Temp)
        List_new.append(v)
    for i in range(0, len(List_new)):
        if List_new[i] not in Check_list:
            Check_list.append(List_new[i])
    for i in range(0, len(Check_list)):
        print "{0}  {1}".format(Check_list[i], List_new.count(Check_list[i]))
		
		# adding a comment