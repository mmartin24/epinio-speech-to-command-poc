file_name = "output.txt"

# Define lists of target words
target_words = {
    "epinio": ["epio", "opinion", "video", "filipino", "happy new year", "athenia", "15", "albino", "peppino", "happy new", "wake me up", "albania", "titanium", "minneapolis", "jalapeno", "the epinio", "epinion", "ocean", "hey epinio", "continue", "video"],
    "push": ["bush", "porsche", "pushing", "pushing up", "who", "question", "play"],
    "app": ["up", "upgrade", "map", "nap"],
    "name": ["called", "named", "with name"],
    "path": ["pass", "bath", "part", "location", "past", "impact"],
    "ignore": [" in ", " im ", " on ", " and ", " hey ", " an ", " with ", " sign "],
    "all": ["ol", "all"],
}

# Read the last line of the file
with open(file_name, 'r') as file:
    lines = file.readlines()
    if lines:
        last_line = lines[-1].strip()
    else:
        last_line = ""

# Process each list of target words
for key, words in target_words.items():
    if key == "ignore":
        replacement = " "
    elif key in ["name", "path", "all"]:
        replacement = "--" + key
    else:
        replacement = key

    for word in words:
        last_line = last_line.replace(word, replacement)

# Write the modified line back to the file
with open(file_name, 'w') as file:
    file.writelines(lines[:-1])  # Remove the old last line

with open(file_name, 'a') as file:
    file.write(last_line + '\n')  # Append the modified line

print('Searching for unrecognized words and attempting to fix them.')
print(f'Reconverting text into => "{last_line}"')
