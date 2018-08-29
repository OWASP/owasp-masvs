# OWASP Mobile Application Security Verification Standard

<a href="https://github.com/OWASP/owasp-masvs/releases/download/1.1/OWASP_Mobile_AppSec_Verification_Standard_v1.1.pdf"><img width=220px align="right" style="float: right;" src="Document/images/masvs-mini-cover.png"></a>

This is the official Github Repository of the OWASP Mobile Application Security Verification Standard (MASVS). The MASVS establishes baseline security requirements for mobile apps that are useful in many scenarios, including:

- In the SDLC - to establish security requirements to be followed by solution architects and developers;
- In mobile app penetration tests - to ensure completeness and consistency in mobile app penetration tests;
- In procurement - as a measuring stick for mobile app security, e.g. in form of questionnaire for vendors;
- Et cetera.

The MASVS is a sister project of the [OWASP Mobile Security Testing Guide](https://github.com/OWASP/owasp-mstg "OWASP Mobile Security Testing Guide").

# Getting the MASVS

PDF downloads are available on the [Releases page](https://github.com/OWASP/owasp-masvs/releases). The current release is [MASVS version 1.1](https://github.com/OWASP/owasp-masvs/releases/download/1.1/OWASP_Mobile_AppSec_Verification_Standard_v1.1.pdf). The MASVS is also available in different languages: 

- [Spanish](https://github.com/OWASP/owasp-masvs/releases/download/1.0-ES/OWASP_Mobile_AppSec_Verification_Standard_v1.0-ES.pdf)  
- [Russian](https://github.com/OWASP/owasp-masvs/releases/download/1.1-RU/OWASP_Mobile_AppSec_Verification_Standard_v1.1-RU.pdf)

## Gitbook

Read it on [Gitbook](https://mobile-security.gitbook.io/masvs/ "GitBook Mobile AppSec Verification Standard"). The book is automatically synchronized with the main repo. 


## Creating ePub

You can use the gitbook command line tool to generate PDF, epub, and other e-book formats, once you have checked out this repo. To generate the epub version you can use the following command

```bash
$ gitbook epub ./ MASVS.epub
```


## Creating a Word Doc

Run <code>generate_document.sh</code> from the repository root directory. This will create a word document in the same directory. Requires [pandoc](http://pandoc.org "Pandoc").


## Exporting to JSON, XML and CSV

The repository contains a Python tool for converting the requirements into various formats. Clone the repo and run <code>export.py</code> from the repository root.

```
export.py [-h] [--format {json,xml,csv}]
```

## Suggestions and Feedback

To report and error or suggest an improvement, please create an [issue](https://github.com/OWASP/owasp-masvs/issues "Github issues").

# How to Contribute

The MASVS is an open source effort and we welcome contributions and feedback. If you want to contribute additional content, or improve existing content, we suggest that you first contact us on the OWASP MSTG Slack channel:

https://owasp.slack.com/messages/project-mobile_omtg/details/

You can sign up here:
 
https://owaspslack.com/

To add or edit content, simply fork the repository and make your changes, then create a pull request when you are finished. We'll review the changes before we merge them with the master branch in the main repo. In case there's conflicting opinions, we'll create an issue for discussing the changes.

# Read Individual Sections of the MASVS Here

* [Header](Document/0x00-Header.md)
* [Foreword](Document/Foreword.md)
* [Frontispiece](Document/0x02-Frontispiece.md)
* [The Mobile Application Security Verification Standard](Document/0x03-Using_the_MASVS.md)
* [Assessment and Verification](Document/0x04-Assessment_and_Certification.md)
* [V1: Architecture, Design and Threat Modeling Requirements](Document/0x06-V1-Architecture_design_and_threat_modelling_requireme.md)
* [V2: Data Storage and Privacy Requirements](Document/0x07-V2-Data_Storage_and_Privacy_requirements.md)
* [V3: Cryptography Requirements](Document/0x08-V3-Cryptography_Verification_Requirements.md)
* [V4: Authentication and Session Management Requirements](Document/0x09-V4-Authentication_and_Session_Management_Requirements.md)
* [V5: Network Communication Requirements](Document/0x10-V5-Network_communication_requirements.md)
* [V6: Environmental Interaction Requirements](Document/0x11-V6-Interaction_with_the_environment.md)
* [V7: Code Quality and Build Setting Requirements](Document/0x12-V7-Code_quality_and_build_setting_requirements.md)
* [V8: Resiliency Against Reverse Engineering Requirements](Document/0x15-V8-Resiliency_Against_Reverse_Engineering_Requirements.md)
* [Appendix A: Glossary](Document/0x90-Appendix-A_Glossary.md)
* [Appendix B: References](Document/0x91-Appendix-B_References.md)
