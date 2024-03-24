file = open("file_handling_assignment.py", "w")

file.write("This is a file. \n")
file.write("Made in python. \n")

number = 7
file.write(str(number) + "\n")

file.close()

print(file)


try:
 new_file = open("file_handling_assignment.py", "a")

 new_file.write("Appending has been done. \n") 
 new_file.write("Added lines. \n")

 number = 2
 new_file.write(str(number) + "\n")

except IOError as e:
  print("Error occured:", e)

finally:
    if 'file' in locals():
        new_file.close()

print(new_file)