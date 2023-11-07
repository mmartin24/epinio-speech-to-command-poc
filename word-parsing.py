file_name = "output.txt"
target_words = ["opinion", "video", "filipino", "happy new year", "athenia", "15", "albino", "peppino"]

# Read the last line of the file
with open(file_name, 'r') as file:
    lines = file.readlines()
    if lines:
        last_line = lines[-1].strip()
    else:
        last_line = ""

# Replace target words with "Epinio" in the last line
for word in target_words:
    last_line = last_line.replace(word, "epinio")

# # Write the modified line back to the file
with open(file_name, 'w') as file:
    file.writelines(lines[:-1])  # Remove the old last line
with open(file_name, 'a') as file:
    file.write(last_line + '\n')  # Append the modified line

print("Last line after replacing target words:", last_line)