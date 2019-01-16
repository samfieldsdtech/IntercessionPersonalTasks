
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
	base_string = "{0} has {1} HP"

	for key in data["Actors"]:
		output_string = base_string.format(
				key, 
				data["Actors"][key]["HP"])
		print(output_string)

	# TODO: Output Weapons with Damagage and Description

	# TODO: Add a new data category along side Actors and Weapons, put in any relevant data.


if __name__ == '__main__':
    main()