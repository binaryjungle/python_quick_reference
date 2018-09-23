#Beginning of the program
print("Beginning Of the Program")
print("")

#file name is stored in variable
ip_file_name = "ip_data.dat"

#endswith meethod cann be used to validate file extensions
if ip_file_name.endswith(".dat"):
    print("Perfect")
else:
    print("Not Perfect")

#open method is used to open the file and mention the mode to open the file
#r means read, w means write, t means text and b means binary 
ip_file = open(ip_file_name, "rt")
op_file = open("op_data_by_etl.dat", "wt")

#mode method will check if open mode is as expected
print("Perfectly" if "r" in ip_file.mode else "not perfect")

#readlines method will read every line in the file which can then be used in for loop
for ip_record in ip_file.readlines():
    print(ip_record) #prints the last newline in each record
    print(ip_record.strip()) #trims the last newline in each record

#we can only perform one operation after one open
#we need to re-open the file for different operation    
ip_file = open(ip_file_name, "rt")

#enumerate adds counter for each loop automatically
for line_number, ip_record in enumerate(ip_file.readlines(),1):
    print(line_number, ip_record.strip())

ip_file = open(ip_file_name, "rt")

#read method reads the full data as such completely
file_data = ip_file.read()
print(file_data)

ip_file = open(ip_file_name, "rt")

for ip_record in ip_file:
    ip_list = str(ip_record.rstrip()).split(sep="|") #strip removes newline, split specifies delimiter and final output is a list 
    op_list = ip_list[0:4]
    op_list.append(f"{int(ip_list[4])*1.07:.0f}")
    #One way of writing data to output files
    #print("|".join(op_list), file=op_file)
    #another way of writing data to output files
    op_file.writelines("|".join(op_list)+"\n")
op_file.close()

ip_file = open(ip_file_name, "rt")
op_file = open("op_data_by_size.dat", "wt")
while True:
    #read input file based on buffer size. Useful for binary files rather than text files.
    ip_buffer = ip_file.read(10)
    if ip_buffer:
        #writes the same buffer into output file
        op_file.write(ip_buffer)
    else:
        break
op_file.close()

#reading binary file
ip_file = open("ip_image.png", "rb")
op_file = open("op_image.png", "wb")
while True:
    ip_buffer = ip_file.read(10240)
    if ip_buffer:
        op_file.write(ip_buffer)
    else:
        break
op_file.close()

#End of the program
print("")
print("End Of the Program")