sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")


print("\nPART 1: Preview with read(40)")
file_part1 = open("class-notes.txt", "r")
content = file_part1.read(40)
print(content)
file_part1.close()


print("\nPART 2: readlines()")
file_part2 = open("class-notes.txt", "r")
lines = file_part2.readlines()
file_part2.close()

print(f"Total lines in file: {len(lines)}")
for i in range(len(lines)):
    print(f"{i + 1} -> {lines[i].strip()}")


print("\nPART 3: Loop line by line")
file_part3 = open("class-notes.txt", "r")
for line in file_part3:
    print(f"Reading: {line.strip()}")
file_part3.close()


print("\nPART 4: Filter with a condition")
file_part4 = open("class-notes.txt", "r")
kept_count = 0
skipped_count = 0

for line in file_part4:
    if line.startswith("SKIP"):
        print(f"Skipped: {line.strip()}")
        skipped_count += 1
    else:
        print(f"Kept: {line.strip()}")
        kept_count += 1
file_part4.close()

print(f"Kept {kept_count} lines and skipped {skipped_count} lines.")


print("\nPART 5: Copy selected lines to a new file")
file_in = open("class-notes.txt", "r")
all_lines = file_in.readlines()
file_in.close()

output_file = open("organized-notes.txt", "w")
copied_count = 0

for line in all_lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        output_file.write(line)
        copied_count += 1
output_file.close()

print(f"Copied {copied_count} lines into 'organized-notes.txt'.")


print("\nPART 6: Organized notes")
file_part6 = open("organized-notes.txt", "r")
for line in file_part6:
    print(line.strip())
file_part6.close()
