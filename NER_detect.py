import spacy

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_sm")

print('done loading model')

# Define the text to be analyzed
text = "Apple Inc. is looking to buy a startup in the autonomous vehicle space. Their CEO is called Hamed Ketabdar who is from Iran\n\nThey are interested in expanding their presence in the transportation industry and believe that acquiring a startup in the autonomous vehicle space will give them a competitive edge."

# Process the text with the NER model
doc = nlp(text)

# Extract named entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print the named entities
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
