from transformers import pipeline

# Use a pre-trained model for Named Entity Recognition
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

print('done loading model')

text = "Apple Inc. is looking to buy a startup in the autonomous vehicle space. Their CEO is called John Tailor who is from Iran\n\nThey are interested in expanding their presence in the transportation industry and believe that acquiring a startup in the autonomous vehicle space will give them a competitive edge."

# Process the text with the NER model
doc = nlp(text)

# Print the named entities
for entity in doc:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}")