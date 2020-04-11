# मूल्यांकन और प्रमाणन

## MASVS प्रमाणन और विश्वास निशान पर OWASP का रुख

OWASP, एक विक्रेता-तटस्थ-फॉर-प्रॉफ़िट संगठन के रूप में, किसी भी विक्रेता, सत्यापनकर्ता या सॉफ़्टवेयर को प्रमाणित नहीं करता है.

ऐसे सभी आश्वासन दावे, विश्वास चिह्न, या प्रमाणपत्र आधिकारिक रूप से OWASP द्वारा प्रमाणित, पंजीकृत या प्रमाणित नहीं हैं, इसलिए इस तरह के दृष्टिकोण पर भरोसा करने वाले एक संगठन को किसी तीसरे पक्ष या ट्रस्ट मार्किंग ट्रस्ट (M) ASVS प्रमाणपत्र  में रखे गए विश्वास से सावधान रहने की आवश्यकता है.

यह संगठनों को ऐसी आश्वासन सेवाओं की पेशकश करने से रोकना नहीं चाहिए, जब तक कि वे आधिकारिक OWASP प्रमाणपत्र का दावा नहीं करते.

## मोबाइल एप्लिकेशन को प्रमाणित करने के लिए मार्गदर्शन

मोबाइल ऐप को पुष्टि करने का अनुशंसित तरीका  है  MASVS के साथ "खुली किताब" समीक्षा करे,
जिसका अर्थ है कि टेस्टर को प्रमुख संसाधनों जैसे कि ऐप के आर्किटेक्ट्स और ऐप के डेवलपर्स जैसे प्रोजेक्ट, प्रोजेक्ट डॉक्यूमेंटेशन, सोर्स कोड और एंडपॉइंट्स के लिए ऑथेंटिकेटेड एक्सेस के लिए हर रोल के लिए कम से कम एक यूजर अकाउंट का एक्सेस दिया जाता है।

यह ध्यान रखना महत्वपूर्ण है कि MASVS केवल (क्लाइंट-साइड) मोबाइल ऐप और उसके दूरस्थ समापन बिंदु(ओं) के बीच नेटवर्क संचार की सुरक्षा को कवर करता है, साथ ही उपयोगकर्ता प्रमाणीकरण और session management से संबंधित कुछ बुनियादी और सामान्य आवश्यकताओं को भी पूरा करता है। इसमें ऐप से जुड़ी दूरस्थ सेवाओं (जैसे वेब सेवाओं) के लिए विशिष्ट आवश्यकताएं नहीं हैं, प्रमाणीकरण और session management से संबंधित सामान्य आवश्यकताओं के सीमित सेट के लिए बचत करें. हालांकि, MASVS V1 निर्दिष्ट करता है कि दूरस्थ सेवाओं को समग्र threat model द्वारा कवर किया जाना चाहिए, और उचित मानकों के खिलाफ सत्यापित किया जाना, जैसे कि OWASP ASVS.

एक certifying organization को किसी भी रिपोर्ट में verification के दायरे को शामिल करना चाहिए (विशेष रूप से यदि एक महत्वपूर्ण key component, out of scope से बाहर हो), verification निष्कर्षों का एकsummary, जिसमें Pass और Fail verification शामिल हैं, जिसमें failed test को solve करने के स्पष्ट संकेत हैं। विस्तृत काम के work papers , screenshots या movies, scripts को मज़बूती से और बार-बार किसी मुद्दे का फायदा उठाने के लिए, और परीक्षण के इलेक्ट्रॉनिक रिकॉर्ड, जैसे कि proxy logs और संबंधित notes जैसे कि cleanup list, को standard industry practice माना जाता है। यह केवल एक tool , run करने और failures पर रिपोर्ट करने के लिए पर्याप्त नहीं है; यह पर्याप्त evidence नहीं देता है कि certifying level पर सभी मुद्दों का test किया गया है और पूर्णतया पूरी तरह से tested है। विवाद के मामले में, यह प्रदर्शित करने के लिए पर्याप्त supportive evidence होना चाहिए कि प्रत्येक verified आवश्यकता का वास्तव में परीक्षण किया गया है।

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

### OWASP Mobile Security Testing Guide (MSTG) का उपयोग करना

OWASP MSTG मोबाइलAppliction की सुरक्षा केverification के लिए एक manual है। यह MASVS में सूचीबद्ध आवश्यकताओं की पुष्टि के लिए तकनीकी प्रक्रियाओं का वर्णन करता है। MSTG में परीक्षण मामलों की एक सूची शामिल होती है, जिनमें से प्रत्येक को MASVS में आवश्यकता के अनुसार बनाया जाता है। जबकि MASVS आवश्यकताएं उच्च-स्तरीय और सामान्य हैं, MSTG प्रति मोबाइल-OS आधार पर गहराई से अनुशंसाएं और testing procedures प्रदान करता है।

### Automated Security Testing Tools की भूमिका

जब भी संभव हो, increase करने के लिए source code scanners और black-box testing tools के उपयोग को प्रोत्साहित किया जाता है। हालांकि केवलautomated tools का उपयोग करके MASVS verification को पूरा करना संभव नहीं है: प्रत्येक Mobile App अलग है, और उपयोग किए जा रहे overall architecture, business logic और रूपरेखाओं के समग्र frameworks, और technological नुकसान को समझना, Security को verify करने के लिए Application में एक अनिवार्य आवश्यकता है।

## अन्य उपयोग

### Security Architecture Guidance के रूप में

मोबाइल एप्लिकेशन सुरक्षा सत्यापन मानक के लिए अधिक सामान्य उपयोगों में से एक सुरक्षा आर्किटेक्ट्स के लिए एक संसाधन के रूप में है। दो प्रमुख सुरक्षा वास्तुकला ढांचे, SABSA या TOGAF, मोबाइल एप्लिकेशन आर्किटेक्चर की समीक्षा को पूरा करने के लिए आवश्यक बहुत सारी जानकारी को याद कर रहे हैं। MASVS का उपयोग उन Gap को भरने के लिए किया जा सकता है जो Security Architects mobile apps के मुद्दों के लिए बेहतर नियंत्रण चुनने के लिए security architects को अनुमति देते हैं.

### Off-the-shelf Secure Coding Checklists प्रतिस्थापन के रूप में

कई organizations MASVS को अपनाने से benefit हो रहे हैं, दो level में से एक को चुनकर, या MASVS को forking करके और domain-specific तरीके से प्रत्येक Application के risk level के लिए जो आवश्यक है उसे बदल सकते हैं। जब तक traceability बनी रहती है, तब तक हम इस प्रकार के forking को Passed करते हैं, ताकि यदि कोई App 4.1 की आवश्यकता से गुजरता है, तो इसका मतलब है कि standard evolves के रूप में same forked copies के लिए भी यही बात है.

### Security Testing Methodologies के लिए एक आधार के रूप में

एक अच्छा Mobile appecurity testing methodology MASVS में सूचीबद्ध सभी आवश्यकताओं को कवर करता है। OWASP Mobile Security Testing Guide (MSTG) प्रत्येक verification के लिए black-box और white-box testing मामलों का वर्णन करता है.

### Automated Unit और integration tests के लिए एक guide के रूप में

MASVS को architectural की आवश्यकताओं के sole exception के साथ, highly testable योग्य बनाया गया है। MASVS आवश्यकताओं के आधार पर Automated unit, integration और acceptance testing निरंतर development lifecycle में integrated किया जा सकता है। यह न केवल developer security awareness बढ़ाता है, बल्कि resulting apps की overall quality में सुधार करता है, और pre-release phase में security testing के दौरान निष्कर्षों की मात्रा को कम करता है.

### सुरक्षित Development Training के लिए

MASVS का उपयोग secure mobile Application की विशेषताओं को द्वारा प्रस्तुत करने के लिए भी किया जा सकता है। कई "secure coding " कोर्स केवल coding tips के हल्के स्मीयर के साथ simply Ethical Hacking courses हैं। यह developers की मदद नहीं करता है। इसके बजाय, secure development course MASVS का उपयोग कर सकते हैं, जैसे कि MASVS में proactive controls documented पर एक strong focus के साथ उपयोग कर सकता है , उदाहरण के लिए- Top 10 code security issues