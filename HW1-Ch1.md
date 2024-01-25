# Homework 1 - Chapter 1 #
### Alex Bryan
### Due Jan 28

---

## Problem 1: Explain the difference between an attack surface and an attack tree.
An attack surface describes the vulnerabilities in a system. Whether these points are network, software, or socially based, recognizing these weaknesses will reveal
how vulnerable a system is. Alternatively, an attack tree is a node-based expression of how an attack could be structured from any vulnerability (notated as a leaf on the attack tree) to the goal (root) of the attack.

---

## Problem 2: Consider an ATM, to which users provide a PIN and a card for account access. Give examples of confidentiality, integrity, and availability requirements asociated with the system and, in each case, indicate the degree of importance if the requirement.
Confidentiality: The PIN and pinpad are not visible to people not standing at the ATM. The displayed pin should be sensored, and any audible noises from pinpad entry
should be monotone. - middle level of importance

Integrity: The user is required to enter their card, then enter the correct PIN. Incorrect PIN entries are limited, and suspicious activity (whether many incorrect entries, or many transactions in a short period of time) should be flagged and the card owner should be notified. The pin pad should be designed such that skimmers
cannot be readily installed. - highest level of importance

Availability: After a user enters a valid card and correct PIN, access to the teller system is granted. A withdrawl request should dispense an equivelent amount of
cash. After a transaction is complete, the account balance is updated and the system returns to asking for a card and PIN. - lowest level of importance

---

## Problem 3: For each of the following assets, assign a low, moderate, or high impact level for the loss of confidentiality, integrity, or availability, respectively. Justify your answers.
### a. An organization managing public information on its Web server.
Low

### b. A law enforcement organization managing extremely sensitive investigative information.
High

### c. A financial organization managing routine administrative information (not privacy related information)
Moderate

### d. An information system used for large acquisitions in a contracting organization contains both sensitive, pre-soliciation phase contract information and routine administrative information. Assess the impact for the two data sets separately and the information system as a whole.
High

### e. A power plant contains a SCADA (supervisory control and data acquisition) system controlling the distribution of electric power for a large military instillation. The SCADA system contains both real-time sensor data and routine administrative information. Assess the impact for the two data sets separately and the information system as a whole.
High

---

## Problem 4: Develop an attack tree for gaining access to the contents of a physical safe.

    └── Open safe
        ├── Pick lock/
        │   ├── Pin-by-pin picking
        │   ├── Check for unshielded core
        │   ├── Shim
        │   └── Check for bump key vulnerability
        ├── Learn combination/
        │   ├── From owner/
        │   │   ├── Ask very politely and definitely without intimidation ;)
        │   │   ├── Socially engineer common combinations/
        │   │   │   ├── Digital scamming
        │   │   │   ├── Befriend the owner, then betray them
        │   │   │   └── Impersonate a safe maintainence crew
        │   │   └── Borrow key
        │   └── From side-channel/
        │       ├── Check for fingerprints on pinpad
        │       ├── Observe owner entering pin discretely/
        │       │   ├── Bug the safe
        │       │   └── Observe in person
        │       └── Look for combination written/typed somewhere
        └── Brute force/
            ├── Drill core
            ├── Cut door open
            ├── Magnetic bypass
            ├── Stellar guessing skills and determination
            └── Melt safe door/wall


## Extra Credit: Provide a reasonable answer for why I might not want a PDF. ##

PDFs are vulnerable to attacks because malicious code can be embeddd into the file to execute unprompted in the background.
Due to Actions, JavaScript embedding, and hyperlinks being added to PDFs in an attempt to make them more powerful, these vulnerabilities opened up. Whether it is adding a dangerous hyperlink, embedding a secret file within the PDF, or adding
JavaScript attacks, PDFs can be equipped with backdoors, keyloggers, IP leaks, and more.

[Reference - trustwave.com](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/threat-loaded-malicious-pdfs-never-go-out-of-style/)
