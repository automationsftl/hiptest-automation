
def get_duplicate_method_index(lines, method_name):
    for index, line in enumerate(lines):
        if line.strip().startswith(method_name):
            return index


f = open("./hiptest/test_project.py", "r", encoding="utf8")
test_lines = f.readlines()
f.close()


f = open("./hiptest/actionwords.py", "r")
actions_lines = f.readlines()
f.close()

previous_deleted = False
for i, action_line in enumerate(actions_lines[12:]):
    index = 12 + i
    if previous_deleted:
        actions_lines[index] = ""
        previous_deleted = False

    if action_line.strip().startswith("def "):
        method_name = action_line.strip().replace("def ", "")
        method_name = "self.actionwords." + method_name[:method_name.index("(")]

        method_exists = False
        for test_line in test_lines:
            if method_name in test_line:
                method_exists = True
                break

        if not method_exists:
            actions_lines[index] = ""
            previous_deleted = True


for index, line in enumerate(actions_lines):
    if line.strip().startswith("def "):
        method_name = line[:line.index("self")]
        duplicate_index = get_duplicate_method_index(actions_lines, method_name.strip())
        if duplicate_index is not None and duplicate_index != index:

            print("duplicate")

            next_line = actions_lines[index+1]
            duplicate_next_line = actions_lines[duplicate_index + 1]

            if next_line.strip() == "pass":
                actions_lines[index] = ""
                actions_lines[index +1] = ""
            elif duplicate_next_line.strip() == "pass":
                actions_lines[duplicate_index] =""
                actions_lines[duplicate_index +1] =""


result_lines = []

previous_text = False
for line in actions_lines:
    if line.strip() != "":
        result_lines.append(line)
        previous_text = True

    if line.strip() == "":
        if previous_text:
            result_lines.append(line)
        previous_text = False


f = open("./hiptest/actionwords_v2.py", "w")
f.writelines(result_lines)
f.close()

