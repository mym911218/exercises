file_name = " Dropbox/895/github/exercises/Romeo and Juliet.txt"
my_file = open( "Romeo and Juliet.txt", "r")

# creat an empty dictionary to put word and count in
counts= dict()

# extract every word from the line (from the file)
for current_line in my_file:
	word_list = current_line.split()
	
# for every word, if this is a new word, and haven't appear in the dictionary, start the count from 1, if this word have already exist in the dictionary, then add 1 into the counts.
	for word in word_list:
		if word not in counts:
			counts[word]= 1
		else:
			counts[word]+= 1
for word in counts:
	print word, counts[word]
