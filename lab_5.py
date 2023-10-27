with open('"/Users/karishmavundavalli/Library/MobileDocuments/com~apple~TextEdit/Documents/AI lab"', 'r') as input_file:
  with open('"/Users/karishmavundavalli/Library/MobileDocuments/com~apple~TextEdit/Documents/AI lab"', 'w') as output_file:
  for line in input_file:
    s1 = line.lower().split(
    s2 = sorted(s1
    sorted_line = ' '.join(s2)
    output_file.write(sorted_line + '\n')
