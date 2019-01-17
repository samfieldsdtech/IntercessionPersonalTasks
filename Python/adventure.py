
"""
This section will be about accessing information inside json files.

How to Run: python adventure.py

Desired Output:

	Contents of example.json should be outputted with new fields added.

"""

import json

def main():
	data = ""
	with open("example.json") as in_file:
		data = json.load(in_file)

	# TODO: Add a field with the key "Description" with a data inside example.json
	# TODO: Output the Description to the console by formatting it with base_string (you will need to edit it)
	base_string = "{0} has {1} HP {0} has {2} MP "
	
	for key in data["Actors"]:
		output_string = base_string.format(
				key, 
				data["Actors"][key]["HP"],
                data ["Actors"][key]["MP"])
		print(output_string)

	# TODO: Output Weapons with Damage and Description
	base_string = "{0} has {1} Damage "
	for key in data["Weapons"]:
		output_string = base_string.format(
				key, 
				data["Weapons"][key]["Damage"])
		print(output_string)        
	# TODO: Add a new data category along side Actors and Weapons, put in any relevant data.
	base_string = "{0} has {1} Damage {0} has {2} HP "
	for key in data["Spells"]:
		output_string = base_string.format(
				key, 
				data["Spells"][key]["Damage"],
				data["Spells"][key]["HP"])
		print(output_string)

if __name__ == '__main__':
    main()