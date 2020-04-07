import spacy
import random


TRAIN_DATA = [('The attacks associated with the new botnet attempted to exploit the CVE-2017-17215 zero-day vulnerability in the Huawei home router caused by the fact that the TR-064 technical report standard, which was designed for local network configuration, was exposed to WAN through port 37215 (UPnP – Universal Plug and Play).', {'entities': [(68, 82, 'SV')]}), ('About 12 hours ago (2017-12-05 11:57 AM GMT+8), we noticed a new version of Satori (a mirai variant which we named Satori), starting to propagate very quickly on port 37215 and 52869.', {'entities': [(162, 182, 'Port')]}), ('Two new exploits, which work on port 37215 and 52869 have been added, see below for more details.', {'entities': [(32, 52, 'Port')]}), ('Due to the worm like behavior, we all should be on the lookout for the port 37215 and 52869 scan traffic.', {'entities': [(71, 91, 'Port')]}), ('For those who don’t have the visibility, feel free to check out our free Scanmon system for port 37215 and 52869, or ISC port pages for 37215 and 52869.', {'entities': [(92, 112, 'Port')]}), ('As can be seen from the following picture, the bot will scan port 37215 and 52869 randomly, determined by the remainder of a random integer mod 3.', {'entities': [(61, 81, 'Port')]}), ('During the scanning, Satori will utilize two different exploits, one on port 37215, while the other on 52869.', {'entities': [(72, 82, 'Port'), (103, 108, 'Port')]}), ('The one on port 37215 is not fully disclosed yet, our team has been tracking this in the last few days and got quite some insight, but we will not discuss it here right now.(stay tuned for our update later).', {'entities': [(11, 21, 'Port')]}), ('For example, during last recent 12 hours we have seen 263,250 different IPs scanning port 37215, and 19,403 IPs scanning port 52869.', {'entities': [(85, 95, 'Port'), (121, 131, 'Port')]}), ('We analyzed another Mirai variant called “Miori,” which is being spread through a Remote Code Execution (RCE) vulnerability in the PHP framework, ThinkPHP.', {'entities': [(82, 123, 'SV')]}), ('For its arrival method, the IoT botnet uses the said exploit that affects ThinkPHP versions prior to 5.0.23 and 5.1.31.', {'entities': [(74, 82, 'SV')]}), ('Our own analysis revealed that the cybercriminals behind Miori used the ThinkPHP RCE to make vulnerable machines download and execute their malware.', {'entities': [(72, 84, 'SV')]}), ('With Mirai Comes Miori: IoT Botnet Delivered via ThinkPHP Remote Code Execution Exploit.', {'entities': [(58, 79, 'SV')]}), ('Miori now spreading via Remote code execution vulnerability in', {'entities': [(24, 45, 'SV')]}), ('The Miori bot borrows the code from the dreaded Mirai malware and it first appeared in the threat landscape in late 2018 when the bot was spread by exploiting a ThinkPHP remote code execution vulnerability after the exploit code was made publicly available. ', {'entities': [(161, 205, 'SV')]}), ('Among the list of devices targeted by the Wicked Mirai are Netgear DGN1000 and DGN2200 v1 routers (also used by Reaper botnet).', {'entities': [(59, 74, 'Model'), (79, 97, 'Model')]}), ('Specifically, port 8080 brings an exploit for a flaw in Netgear DGN1000 and DGN2200 v1 routers (also used by the Reaper botnet).', {'entities': [(56, 71, 'Model'), (76, 86, 'Model')]}), ('On port 8080, the malware uses Netgear DGN1000 and DGN2200 v1 router exploits (also used by Reaper botnet).', {'entities': [(31, 46, 'Model'), (51, 68, 'Model')]}), ('If connected to Port 8080, the malware will use a remote code execution (RCE) Netgear exploit which works on DGN1000 and DGN2200 v1 routers, and is the same tool used by the Reaper botnet to compromise target machines.', {'entities': [(50, 77, 'SV'), (16, 25, 'Port'), (109, 116, 'Model'), (121, 139, 'Model')]}), ('On port 8080, Netgear DGN1000 and DGN2200 v1 router exploits are used, a CCTV-DVR remote code execution exploit is used on port 81, ', {'entities': [(3, 12, 'Port'), (14, 29, 'Model'), (34, 51, 'Model'), (82, 103, 'SV'), (123, 130, 'Port')]}), ('Below is a list of devices targeted by the Wicked Mirai; Port 8080: Netgear DGN1000 and DGN2200 v1 routers.', {'entities': [(57, 66, 'Port'), (68, 83, 'Model'), (88, 106, 'Model')]}), ('Devices Targeted by Wicked include Netgear DGN1000 and DGN2200 v1 routers on Port 8080.', {'entities': [(35, 50, 'Model'), (55, 73, 'Model'), (77, 86, 'Port')]}), ('The dissection of this suspicious file, known by Symantec as Trojan.Emotet, shows common elements such as: TCP communication over ports 80, 8080, 22,990.', {'entities': [(130, 152, 'Port')]}), ('Emotet connects to C2 servers on various ports including, but not limited to: 20, 80, 443, 7080, 8443, and 50000', {'entities': [(78, 112, 'Port')]}), ('We can see that port 80 returns the same universal 404 error as the hacked server did on the Emotet port, so most likely this is the port it forwards traffic to.', {'entities': [(16, 23, 'Port')]}), ('The C2 servers can receive these communications on port 80, which is the default port for HTTP, but may also receive them on port 443, which is the default for HTTPS traffic, or on a number of other nonstandard ports, including but not limited to 7080, 8080, 8090, 50000, or several others. ', {'entities': [(51, 58, 'Port'), (247, 270, 'Port')]}), ('The initial executable appears to launch an application application lpiograd.exe, seen in Figure 2 and then looks to make outbound network connections on port 80, to a single command and control (CnC) server', {'entities': [(154, 161, 'Port')]}), ('Emotet Trojan used commonly used port for communication (e.g TCP port 80, 8080, 443, 8443, 7080, 20, 22, 53)', {'entities': [(61, 107, 'Port')]}), ('5.101.138.188 port 80 - sloegincottage.co.uk - GET /tyoinvur/En_us/Clients/092018/', {'entities': []})]


def train_spacy(data,iterations):
    TRAIN_DATA = data
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
       

    # add labels
    for _, annotations in TRAIN_DATA:
         for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Statring iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp


prdnlp = train_spacy(TRAIN_DATA, 20)

# Save our trained Model
modelfile = input("Enter your Model Name: ")
prdnlp.to_disk(modelfile)

#Test your text
test_text = input("Enter your testing text: ")
doc = prdnlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)