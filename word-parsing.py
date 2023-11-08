file_name = "output.txt"
target_words_epinio = ["epio","opinion", "video", "filipino", "happy new year", "athenia", "15", "albino", "peppino", "happy new", "wake me up", "albania", "titanium", "minneapolis", "jalapeno" , "the epinio", "epinion", "ocean", "hey epinio"]
target_words_push = ["bush","porsche", "push an app", "pushing" "push up", "pushing up", "who"]
target_words_app = ["up","upgrade"]
target_words_path = ["pass", "bath", "part", "location", "past", "impact"]
target_words_name = ["called", "name", "named", "with name"]
target_words_ignore = [" in ", " im ", " on ", " and " ," hey ", " an ", " with ", " sign "]

# Read the last line of the file
with open(file_name, 'r') as file:
    lines = file.readlines()
    if lines:
        last_line = lines[-1].strip()
    else:
        last_line = ""

# Replace target words with "Epinio" in the last line
for word in target_words_epinio:
    last_line = last_line.replace(word, "epinio")

# if target_words_push:
for word in target_words_push:
    last_line = last_line.replace(word, "push")

# if target_words_app:
for word in target_words_app:
    last_line = last_line.replace(word, "app")

# if target_words_name:
for word in target_words_name:
    last_line = last_line.replace(word, "--"+"name")

# if target_words_path
for word in target_words_path:
    last_line = last_line.replace(word, "--"+"path")

# Cleansing of some articles and other words by a space
for word in target_words_ignore:
    last_line = last_line.replace(word, " ")

# # Write the modified line back to the file
with open(file_name, 'w') as file:
    file.writelines(lines[:-1])  # Remove the old last line
with open(file_name, 'a') as file:
    file.write(last_line + '\n')  # Append the modified line

print ('Searching for unrecognized words and attempting to fix them.\n' f'Reconverting text into => "{last_line}"')
