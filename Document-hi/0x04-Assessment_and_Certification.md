# Assessment and Certification
# मूल्यांकन और प्रमाणन

## OWASP's Stance on MASVS Certifications and Trust Marks
## MASVS प्रमाणन और विश्वास निशान पर OWASP का रुख

OWASP, as a vendor-neutral not-for-profit organization, does not certify any vendors, verifiers or software.
OWASP, एक विक्रेता-तटस्थ-फॉर-प्रॉफ़िट संगठन के रूप में, किसी भी विक्रेता, सत्यापनकर्ता या सॉफ़्टवेयर को प्रमाणित नहीं करता है.

All such assurance assertions, trust marks, or certifications are not officially vetted, registered, or certified by OWASP, so an organization relying upon such a view needs to be cautious of the trust placed in any third party or trust mark claiming (M)ASVS certification.
ऐसे सभी आश्वासन दावे, विश्वास चिह्न, या प्रमाणपत्र आधिकारिक रूप से OWASP द्वारा प्रमाणित, पंजीकृत या प्रमाणित नहीं हैं, इसलिए इस तरह के दृष्टिकोण पर भरोसा करने वाले एक संगठन को किसी तीसरे पक्ष या ट्रस्ट मार्किंग ट्रस्ट (M) ASVS प्रमाणपत्र  में रखे गए विश्वास से सावधान रहने की आवश्यकता है.

This should not inhibit organizations from offering such assurance services, as long as they do not claim official OWASP certification.
यह संगठनों को ऐसी आश्वासन सेवाओं की पेशकश करने से रोकना नहीं चाहिए, जब तक कि वे आधिकारिक OWASP प्रमाणपत्र का दावा नहीं करते.

## Guidance for Certifying Mobile Apps
## मोबाइल एप्लिकेशन को प्रमाणित करने के लिए मार्गदर्शन

The recommended way of verifying compliance of a mobile app with the MASVS is by performing an "open book" review, meaning that the testers are granted access to key resources such as architects and developers of the app, project documentation, source code, and authenticated access to endpoints, including access to at least one user account for each role.
मोबाइल ऐप को पुष्टि करने का अनुशंसित तरीका  है  MASVS के साथ "खुली किताब" समीक्षा करे,
जिसका अर्थ है कि टेस्टर को प्रमुख संसाधनों जैसे कि ऐप के आर्किटेक्ट्स और ऐप के डेवलपर्स जैसे प्रोजेक्ट, प्रोजेक्ट डॉक्यूमेंटेशन, सोर्स कोड और एंडपॉइंट्स के लिए ऑथेंटिकेटेड एक्सेस के लिए हर रोल के लिए कम से कम एक यूजर अकाउंट का एक्सेस दिया जाता है।

It is important to note that the MASVS only covers security of the (client-side) mobile app and the network communication between the app and its remote endpoint(s), as well as a few basic and generic requirements related to user authentication and session management. It does not contain specific requirements for the remote services (e.g. web services) associated with the app, save for a limited set of generic requirements pertaining to authentication and session management. However, MASVS V1 specifies that remote services must be covered by the overall threat model, and be verified against appropriate standards, such as the OWASP ASVS.
यह ध्यान रखना महत्वपूर्ण है कि MASVS केवल (क्लाइंट-साइड) मोबाइल ऐप और उसके दूरस्थ समापन बिंदु(ओं) के बीच नेटवर्क संचार की सुरक्षा को कवर करता है, साथ ही उपयोगकर्ता प्रमाणीकरण और session management से संबंधित कुछ बुनियादी और सामान्य आवश्यकताओं को भी पूरा करता है। इसमें ऐप से जुड़ी दूरस्थ सेवाओं (जैसे वेब सेवाओं) के लिए विशिष्ट आवश्यकताएं नहीं हैं, प्रमाणीकरण और session management से संबंधित सामान्य आवश्यकताओं के सीमित सेट के लिए बचत करें. हालांकि, MASVS V1 निर्दिष्ट करता है कि दूरस्थ सेवाओं को समग्र threat model द्वारा कवर किया जाना चाहिए, और उचित मानकों के खिलाफ सत्यापित किया जाना, जैसे कि OWASP ASVS.

A certifying organization must include in any report the scope of the verification (particularly if a key component is out of scope), a summary of verification findings, including passed and failed tests, with clear indications of how to resolve the failed tests. Keeping detailed work papers, screenshots or movies, scripts to reliably and repeatedly exploit an issue, and electronic records of testing, such as intercepting proxy logs and associated notes such as a cleanup list, is considered standard industry practice. It is not sufficient to simply run a tool and report on the failures; this does not provide sufficient evidence that all issues at a certifying level have been tested and tested thoroughly. In case of dispute, there should be sufficient supportive evidence to demonstrate that every verified requirement has indeed been tested.
एक certifying organization को किसी भी रिपोर्ट में verification के दायरे को शामिल करना चाहिए (विशेष रूप से यदि एक महत्वपूर्ण key component, out of scope से बाहर हो), verification निष्कर्षों का एकsummary, जिसमें Pass और Fail verification शामिल हैं, जिसमें failed test को solve करने के स्पष्ट संकेत हैं। विस्तृत काम के work papers , screenshots या movies, scripts को मज़बूती से और बार-बार किसी मुद्दे का फायदा उठाने के लिए, और परीक्षण के इलेक्ट्रॉनिक रिकॉर्ड, जैसे कि proxy logs और संबंधित notes जैसे कि cleanup list, को standard industry practice माना जाता है। यह केवल एक tool , run करने और failures पर रिपोर्ट करने के लिए पर्याप्त नहीं है; यह पर्याप्त evidence नहीं देता है कि certifying level पर सभी मुद्दों का test किया गया है और पूर्णतया पूरी तरह से tested है। विवाद के मामले में, यह प्रदर्शित करने के लिए पर्याप्त supportive evidence होना चाहिए कि प्रत्येक verified आवश्यकता का वास्तव में परीक्षण किया गया है।

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

### Using the OWASP Mobile Security Testing Guide (MSTG)
### OWASP Mobile Security Testing Guide (MSTG) का उपयोग करना

The OWASP MSTG is a manual for testing the security of mobile apps. It describes the technical processes for verifying the requirements listed in the MASVS. The MSTG includes a list of test cases, each of which map to a requirement in the MASVS. While the MASVS requirements are high-level and generic, the MSTG provides in-depth recommendations and testing procedures on a per-mobile-OS basis.
OWASP MSTG मोबाइलAppliction की सुरक्षा केverification के लिए एक manual है। यह MASVS में सूचीबद्ध आवश्यकताओं की पुष्टि के लिए तकनीकी प्रक्रियाओं का वर्णन करता है। MSTG में परीक्षण मामलों की एक सूची शामिल होती है, जिनमें से प्रत्येक को MASVS में आवश्यकता के अनुसार बनाया जाता है। जबकि MASVS आवश्यकताएं उच्च-स्तरीय और सामान्य हैं, MSTG प्रति मोबाइल-OS आधार पर गहराई से अनुशंसाएं और testing procedures प्रदान करता है।

### The Role of Automated Security Testing Tools
### Automated Security Testing Tools की भूमिका

The use of source code scanners and black-box testing tools is encouraged in order to increase efficiency whenever possible. It is however not possible to complete MASVS verification using automated tools alone: Every mobile app is different, and understanding the overall architecture, business logic, and technical pitfalls of the specific technologies and frameworks being used, is a mandatory requirement to verify security of the app.
जब भी संभव हो, increase करने के लिए source code scanners और black-box testing tools के उपयोग को प्रोत्साहित किया जाता है। हालांकि केवलautomated tools का उपयोग करके MASVS verification को पूरा करना संभव नहीं है: प्रत्येक Mobile App अलग है, और उपयोग किए जा रहे overall architecture, business logic और रूपरेखाओं के समग्र frameworks, और technological नुकसान को समझना, Security को verify करने के लिए Application में एक अनिवार्य आवश्यकता है।

## Other Uses
## अन्य उपयोग

### As Detailed Security Architecture Guidance
### Security Architecture Guidance के रूप में

One of the more common uses for the Mobile Application Security Verification Standard is as a resource for security architects. The two major security architecture frameworks, SABSA or TOGAF, are missing a great deal of information that is necessary to complete mobile application security architecture reviews. MASVS can be used to fill in those gaps by allowing security architects to choose better controls for issues common to mobile apps.
मोबाइल एप्लिकेशन सुरक्षा सत्यापन मानक के लिए अधिक सामान्य उपयोगों में से एक सुरक्षा आर्किटेक्ट्स के लिए एक संसाधन के रूप में है। दो प्रमुख सुरक्षा वास्तुकला ढांचे, SABSA या TOGAF, मोबाइल एप्लिकेशन आर्किटेक्चर की समीक्षा को पूरा करने के लिए आवश्यक बहुत सारी जानकारी को याद कर रहे हैं। MASVS का उपयोग उन Gap को भरने के लिए किया जा सकता है जो Security Architects mobile apps के मुद्दों के लिए बेहतर नियंत्रण चुनने के लिए security architects को अनुमति देते हैं.

### As a Replacement for Off-the-shelf Secure Coding Checklists
### Off-the-shelf Secure Coding Checklists प्रतिस्थापन के रूप में

Many organizations can benefit from adopting the MASVS, by choosing one of the two levels, or by forking MASVS and changing what is required for each application's risk level in a domain-specific way. We encourage this type of forking as long as traceability is maintained, so that if an app has passed requirement 4.1, this means the same thing for forked copies as the standard evolves.
कई organizations MASVS को अपनाने से benefit हो रहे हैं, दो level में से एक को चुनकर, या MASVS को forking करके और domain-specific तरीके से प्रत्येक Application के risk level के लिए जो आवश्यक है उसे बदल सकते हैं। जब तक traceability बनी रहती है, तब तक हम इस प्रकार के forking को Passed करते हैं, ताकि यदि कोई App 4.1 की आवश्यकता से गुजरता है, तो इसका मतलब है कि standard evolves के रूप में same forked copies के लिए भी यही बात है.

### As a Basis for Security Testing Methodologies
### Security Testing Methodologies के लिए एक आधार के रूप में

A good mobile app security testing methodology should cover all requirements listed in the MASVS. The OWASP Mobile Security Testing Guide (MSTG) describes black-box and white-box test cases for each verification requirement.
एक अच्छा Mobile appecurity testing methodology MASVS में सूचीबद्ध सभी आवश्यकताओं को कवर करता है। OWASP Mobile Security Testing Guide (MSTG) प्रत्येक verification के लिए black-box और white-box testing मामलों का वर्णन करता है.

### As a Guide for Automated Unit and Integration Tests
### Automated Unit और integration tests के लिए एक guide के रूप में

The MASVS is designed to be highly testable, with the sole exception of architectural requirements. Automated unit, integration and acceptance testing based on the MASVS requirements can be integrated in the continuous development lifecycle. This not only increases developer security awareness, but also improves the overall quality of the resulting apps, and reduces the amount of findings during security testing in the pre-release phase.
MASVS को architectural की आवश्यकताओं के sole exception के साथ, highly testable योग्य बनाया गया है। MASVS आवश्यकताओं के आधार पर Automated unit, integration और acceptance testing निरंतर development lifecycle में integrated किया जा सकता है। यह न केवल developer security awareness बढ़ाता है, बल्कि resulting apps की overall quality में सुधार करता है, और pre-release phase में security testing के दौरान निष्कर्षों की मात्रा को कम करता है.

### For Secure Development Training
### सुरक्षित Development Training के लिए

MASVS can also be used to define characteristics of secure mobile apps. Many "secure coding" courses are simply ethical hacking courses with a light smear of coding tips. This does not help developers. Instead, secure development courses can use the MASVS, with a strong focus on the proactive controls documented in the MASVS, rather than e.g. the Top 10 code security issues.
MASVS का उपयोग secure mobile Application की विशेषताओं को द्वारा प्रस्तुत करने के लिए भी किया जा सकता है। कई "secure coding " कोर्स केवल coding tips के हल्के स्मीयर के साथ simply Ethical Hacking courses हैं। यह developers की मदद नहीं करता है। इसके बजाय, secure development course MASVS का उपयोग कर सकते हैं, जैसे कि MASVS में proactive controls documented पर एक strong focus के साथ उपयोग कर सकता है , उदाहरण के लिए- Top 10 code security issues.