file_name = " Dropbox/895/github/exercises/Romeo and Juliet.txt"
my_file = open( "Romeo and Juliet.txt", "r")

count_line = 0
count_word = 0
count_character = 0

for current_line in my_file:
	count_line += 1
	print("This is the number \"" + str(count_line) + "\"line in this file.")
	word_list = current_line.split()

	for current_word in word_list:
		count_word += 1
    # another easeir way to count the number of words in a senctence
	count_word2= len( word_list )
	print("There are\"" + str(count_word) + "\"words until now.")
	
	count_character = count_character + len(current_line)


print( "There are\"" + str(count_line) + "\"lines in this file." )

print("There are\"" + str(count_word) + "\"words in this file.")

print("There are\"" + str(count_character) + "\"characters in this file.")

