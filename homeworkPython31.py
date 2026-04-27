import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
patterns = r"\d{2}/\d{2}/\d{4}|\d{2}.\d{2}.\d{4}|\d{2}-\d{2}-\d{4}"


print(re.findall(patterns, text))


#-----------------------------------------------------------------------------------------------------------------------



tag_input = "python. data-science / machine-learning; AI    neural-networks" #input("Input something: ")

print(re.split(r"[/,\s.;:]+", tag_input))
