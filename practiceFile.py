# with open("practice.txt", "w") as f:
#     f.write("Hello, World!\nHi everyone")
#     f.write("This is a test file.\nand so on.")


# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "python")
# print(new_data)    

# def check_for_word():
#      with open("practice.txt", "r") as f:
#       data = f.read()
#       if(data.find("java") == -1):
#         print("java not found")
#       else:
#         print("java found")    

# check_for_word() 

def check_for_line():
    word = "so"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1  
check_for_line()      
            
        

