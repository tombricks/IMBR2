import os
states = [553,554,680,677,799,741,286,670,671]
for filename in os.listdir('states'):
    r_filename = filename.replace(" ", "")
    for state in states:
        if str(state)+"-" in r_filename:
            text = ""
            with open("states/"+filename, mode='r') as file:
                text = file.read()
            text = text.replace("owner = ", "owner = ENG #")
            print(text)
            input()
            with open("states/"+filename, mode='w') as file:
                file.write(text)
