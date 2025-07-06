**REPOSITORY CONTENT**

# limpiar_batch.py

This Python script processes all .json files in a specified folder. For each file, it removes any occurrence of the file's name (without the .json extension) from the JSON content, including its variations with accents or capitalization. It also removes HTML tags and URLs from text fields. The cleaned data is saved into a new file with _limpio added to the original filename.


# sinHTML.py

This Python script processes all .json files in a given folder by removing HTML content, email addresses, certain links, and unnecessary whitespace from the text values. It extracts only the cleaned text values (without keys) and saves them into new JSON files in a separate output folder, each prefixed with limpio_.

# transformar_excel_json.py

This script reads an Excel file containing a list of municipalities and, for each one, loads a corresponding JSON file with additional data. It adds the JSON content to a new column called 'Web' in the DataFrame. Then, it builds a final dictionary where each municipality is a key and its associated data (including the JSON) is the value. Finally, it saves this structured data into a single output JSON file.

# AlicantePublicAdmin_Survey-DTI-Web.zip

This file contains information from surveys conducted with 79 municipalities in the province of Alicante (Spain), prepared by CENID, the University of Alicante, and the Provincial Council of Alicante. Additionally, for each municipality, it includes its level of digitalization—calculated using a formula developed by the creators of the questionnaire based on weighted responses—as well as its corresponding website.
