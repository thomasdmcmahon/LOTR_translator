"""
postprocess.py
---------------
Post-processing translations to correct Lord of the Rings-specific terms.
"""

import re


def postprocess(input_file, translation_file, new_translation_file):
    """Replace incorrect names/terms with correct English counterparts."""
    lotr_names = {
        "Beutlin": "Baggins",
        "Samweis Gamdschie": "Samwise Gamgee",
        "Samweis": "Samwise",
        "Gandalf der Graue": "Gandalf the Grey",
        "Herr Unterberg": "Mr. Underhill",
        "Saruman der Weise": "Saruman the Wise",
        "Auenland": "Shire",
        "Bruchtal": "Rivendell",
        "Graufurt": "Greyflood",
        "Wetterspitze": "Weathertop",
        "Schicksalsberg": "Mount Doom",
        "Nebelgebirge": "Misty Mountains",
        "Isengart": "Isengard",
        "Minas Morgul": "Minas Morgul",
        "Barad-dúr": "Barad-dûr",
        "Orks": "Orcs",
        "Elben": "Elves",
        "Hobbits": "Hobbits",
        "Hobbit": "Hobbit",
        "Gemeinsprache": "Common Tongue",
        "Dunkle Herrscher": "Dark Lord",
        "Mittelerdes": "Middle-earth",
        "Palantír": "Palantir"
    }

    patterns = {re.compile(r'(?<!\w)' + re.escape(de) + r'(?!\w)'): en for de, en in lotr_names.items()}
    changes_made = 0

    with open(translation_file, "r", encoding="utf-8") as infile, \
         open(new_translation_file, "w", encoding="utf-8") as outfile:
        for line_num, line in enumerate(infile, 1):
            for pattern, replacement in patterns.items():
                new_line = pattern.sub(replacement, line)
                if new_line != line:
                    changes_made += 1
                line = new_line
            outfile.write(line)

    print(f"Total changes made: {changes_made}")


if __name__ == "__main__":
    postprocess("data/lotr.de", "results/lotr_output.en", "results/lotr_corrected.en")
