import spacy

TEST_DATA = ['Sometimes just mentioning the new target DGN2730 is enough.', 'We can still identify if Miori now targets DGN2030 Netgear routers.', 'Emotet has new targets like DGN3000 v3 routers', 'Among the list of devices targeted by the Wicked Mirai are Netgear DGN1000 and DGN2200 v1 routers (also used by Reaper botnet).', 'DGN1000 is a model Emotet targets, see if we can identify it', 'If Mirai targets more Netgear routers, we can detect it', 'Mirai targets a new PHP vulnerability discovered recently', 'Emotet\'s RCE vulnerability is detectable', 'Even in other formats like this: Yowai vairant exploits ports 80, 9999, 43 and 60008', 'This Spacy model can extract port 33567 and 40421/tcp', 'The new malware has been found to target port 22', 'According to researchers, Wicked bot now attacks ports 80 and 9999']

output_dir = 'IOC_model'

# test the saved model
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
for text in TEST_DATA:
    doc = nlp2(text)
    print("TEXT:", text)

    for ent in doc.ents:
        value = ent.text
        label = ent.label_
        print("VALUE:", value)
        print("LABEL:", label)
    print()
    # print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    # print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    # with open('PREDS.txt', 'a') as f:
    #     f.write("TEXT: " + text + '\n')
    #     f.write("VALUE: " + value + '\n')
    #     f.write("LABEL: " + label + '\n\n')


