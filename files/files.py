my_file = open('data.txt', 'r')

file_content = my_file.read()

my_file.close()

print(file_content)


username = input('Enter your name: ')

my_file_writing = open('data.txt', 'a')
my_file_writing.write(username)
my_file_writing.close()

print(file_content)

