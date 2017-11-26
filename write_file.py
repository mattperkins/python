# 'w' = write
with open('write.txt', 'w') as write_file:
    write_file.write("This has been written from write_file.py")
    print('Data has been written to the file: "write.txt"')

# 'a' = append
with open('write.txt', 'a') as write_file:
    write_file.write("\nSecond line added")
    print('More Data has been written to the file: "write.txt"')


quotes = [
    "\nFailure is the gateway to success",
    "\nKnoweth the man, knoweth the history"
]
with open('write.txt', 'a') as write_file:
    write_file.writelines(quotes)
    print('Quote data written to "write.txt"')

 