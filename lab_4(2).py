def calculate_similarity(file1, file2):
with open(file1, 'r') as f1, open(file2, 'r') as f2:
text1 = f1.read()
text2 = f2.read()

words1 = text1.split()
words2 = text2.split()
common_words = len([item for item in words1 if item in words2])
total_words = len(words1) + len(words2)
if total_words == 0:
return 0
else:
similarity = common_words / total_words
return similarity

file1_path = "/Users/karishmavundavalli/Downloads/datainfile.txt"
file2_path = "/Users/karishmavundavalli/Downloads/datainfile2.txt"
similarity_index = calculate_similarity(file1_path, file2_path)
print(f"Similarity Index: {similarity_index:.2f}")
