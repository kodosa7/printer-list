# printer list
# scraps txt file for printers and outputs their list
import re


with open("directory.txt", "r") as file:
    content = file.read()

printer_name = "WF-C5710"
room_list = []
count = content.count(printer_name)

print("Number of", printer_name, "printers:", count // 2)

new_list = []

# finds and extracts needed string
for match in re.finditer("WF-C5710", content):
    string = str(match)
    split_string = string.split()
    my_string = split_string[2]
    out_string_left = "span=("
    out_string_right = ","

    number_strip_one = my_string.strip(out_string_left)
    number = int(number_strip_one.strip(out_string_right))
    
    for i in range(len(content)):
        if i == number:
            new_list.append(content[number - 17:number + len(printer_name)])
        
# converts list to set (to delete duplicates)
final_list = list(set(new_list))

# writes result to a new file
with open("result.txt", "w") as wfile:
    for i in final_list:
        print(i, file=wfile)

print("File result.txt created")
print("Done")