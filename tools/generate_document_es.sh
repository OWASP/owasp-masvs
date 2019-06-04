#!/bin/bash
type pandoc >/dev/null 2>&1 || { echo >&2 "I require pandoc but it's not installed.  Aborting."; exit 1; }
# How to generate Docx
cd ../Document-es
pandoc -f markdown_github --toc -N --columns 10000 --self-contained -s --reference-doc ../Tools/reference.docx -t docx -o ../Generated/MASVS-es.docx \
0x00-Header.md \
Changelog.md \
Foreword.md \
0x02-Frontispiece.md \
0x03-Using_the_MASVS.md \
0x04-Assessment_and_Certification.md \
0x06-V1-Architecture_design_and_threat_modelling_requireme.md \
0x07-V2-Data_Storage_and_Privacy_requirements.md \
0x08-V3-Cryptography_Verification_Requirements.md \
0x09-V4-Authentication_and_Session_Management_Requirements.md \
0x10-V5-Network_communication_requirements.md \
0x11-V6-Interaction_with_the_environment.md \
0x12-V7-Code_quality_and_build_setting_requirements.md \
0x15-V8-Resiliency_Against_Reverse_Engineering_Requirements.md \
0x90-Appendix-A_Glossary.md \
0x91-Appendix-B_References.md
cd ..
# how to generate pdf
#cd Document
#pandoc --latex-engine=xelatex -o ../MASVS.pdf *.md
#cd ..
