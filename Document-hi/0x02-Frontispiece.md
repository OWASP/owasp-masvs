# About the Standard

## मानक के बारे में

<img src="images/OWASP_logo.png" title="OWASP LOGO" />

Welcome to the Mobile Application Security Verification Standard (MASVS) 1.1. The MASVS is a community effort to establish a framework of security requirements needed to design, develop and test secure mobile apps on iOS and Android.

मोबाइल एप्लिकेशन सुरक्षा सत्यापन मानक (MASVS) 1.1 में आपका स्वागत है। MASVS आईओएस (iOS) और एंड्रॉइड पर सुरक्षित मोबाइल एप्लिकेशन को डिजाइन, विकसित और परीक्षण करने के लिए आवश्यक सुरक्षा आवश्यकताओं के ढांचे को स्थापित करने का एक सामुदायिक प्रयास है।

The MASVS is a culmination of community effort and industry feedback. We expect this standard to evolve over time and welcome feedback from the community.

MASVS सामुदायिक प्रयास और उद्योग की प्रतिक्रिया के चरम बिंदु है। हम उम्मीद करते हैं कि यह मानक समय के साथ विकसित होगा और समुदाय से प्रतिक्रिया का स्वागत करेगा।

The best way to get in contact with us is via the OWASP Mobile Project Slack channel: <https://owasp.slack.com/messages/project-mobile_omtg/details/> .

हमारे साथ संपर्क करने का सबसे अच्छा तरीका OWASP मोबाइल प्रोजेक्ट स्लैक चैनल है: <https://owasp.slack.com/messages/project-mobile_omtg/details/> .

Accounts can be created at the following URL: [https://owasp-slack.herokuapp.com/](https://owasp-slack.herokuapp.com/).

निम्नलिखित URL पर खाते बनाए जा सकते हैं: [https://owasp-slack.herokuapp.com/](https://owasp-slack.herokuapp.com/).

## Copyright and License

## कॉपीराइट और लाइसेंस

[<img src="images/CC-license.png" title="License" width="200px" height="45px" />](https://creativecommons.org/licenses/by-sa/4.0/)

Copyright © 2020 The OWASP Foundation.This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). For any reuse or distribution, you must make clear to others the license terms of this work.

कॉपीराइट © 2020 OWASP Foundation.यह काम एक [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) के तहत लाइसेंस प्राप्त है। किसी भी तरह के पुन: उपयोग या वितरण के लिए, आपको इस कार्य के लाइसेंस की शर्तों को दूसरों को स्पष्ट करना चाहिए।

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>


## Acknowledgements

## आभार

| Project Lead | Lead Author | Contributors and Reviewers
| ------- | --- | ----------------- |
| Sven Schleier, Jeroen Willemsen and Carlos Holguera | Bernhard Mueller | Alexander Antukh, Mesheryakov Aleksey, Bachevsky Artem, Jeroen Beckers, Vladislav Chelnokov, Ben Cheney, Peter Chi, Lex Chien, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, Tereshin Dmitry, Christian Dong, Oprya Egor, Ben Gardiner, Rocco Gränitz, Henry Hu, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, Gall Maxim, Eugen Martynov, Riotaro Okada, Abhinav Sejpal, Stefaan Seys, Yogesh Sharma, Prabhant Singh, Sven Schleier, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Romuald Szkudlarek, Abderrahmane Aftahi, Abdessamad Temmar, Koki Takeyama, Chelnokov Vladislav, Leo Wang|

|  प्रोजेक्ट लीड  |  लीड लेखक  |  योगदानकर्ता और समीक्षक  |
|  ---------  |  ---------  |  -------------------  |
|स्वेन श्लेयर, जेरोएन विल्मसेन और कार्लोस होलगुएरा|बर्नहार्ड मुलर| अलेक्जेंडर एंटुख, मेशरीकोव एलेक्सी, बेचेवस्की आर्टेम, जीरोके बेकर्स, व्लादिस्लाव चेल्नोकोव, बेन चेनी, पीटर ची, लेक्स चेयन, स्टीफन कोर्बियाक्स, मैनुअल डेलगाडो, राचेंको डेनिस, रेयान डेहर्स्ट, टेराशिन दिमित्री, क्रिश्चियन डोंग, ओप्री एगोर, बेन गार्डिनर, आर गार्डेनर। , हेनरी हू, सोज़ेरड लैंगकम्पर, विनीसस हेनरिक मारंगोनी, मार्टिन मार्सिकोनो, रॉबर्टो मार्टेलोनी, गैल मैक्सिम, यूजेन मार्टीनोव, रियोटारो ओकाडा, अभिनव सेजपाल, स्टेफन सीस, योगेश शर्मा, प्रभात सिंह, स्वेन श्लेयर, निखिल सोनी, अनीता सोनी, अनीता सोनी। रोमुआल्ड स्ज़ुडलारेक, एबदर्रहमान आफ़ताही, अब्देसमद तमार, कोकी पाइयामा, चेलनोकोव व्लादिस्लाव, लियो वांग |
<br/>

| Language | Translators & Reviewers |
| --- | ------------------------------ |
| Chinese (Traditonal) | Peter Chi, and Lex Chien, Henry Hu, Leo Wang |
| Chinese (Simplified) | Bob Peng, Harold Zang, Jack S |
| French | Romuald Szkudlarek, Abderrahmane Aftahi, Christian Dong (Review) |
| German | Rocco Gränitz, Sven Schleier (Review) |
| Japanese | Koki Takeyama, Riotaro Okada (Review) |
| Korean | Youngjae Jeon, Jeongwon Cho, Jiyou Han, Jiyeon Sung |
| Russian | Gall Maxim, Eugen Martynov, Chelnokov Vladislav (Review), Oprya Egor (Review), Tereshin Dmitry (Review) |
| Spanish | Martin Marsicano, Carlos Holguera |
| Hindi   | Mukesh Sharma, Kunwar Atul Singh, Ritesh Kumar, Vikrant Shah, Devendra Kumar Sinha, Parag Dave|

This document started as a fork of the OWASP Application Security Verification Standard written by Jim Manico.

| भाषा  | अनुवादक और समीक्षक |
| --- | ------------------  |
| चीनी (पारंपरिक)| पीटर ची, और लेक्स चिएन, हेनरी हू, लियो वांग|
| चीनी (सरलीकृत)| बॉब पेंग, हेरोल्ड ज़ैंग, जैक एस|
| फ्रेंच | रोमुआल्ड स्ज़ुडलारेक, एबदर्रहमान आफ़ताही, क्रिश्चियन डोंग (समीक्षा)|
| जर्मन | रोक्को ग्रिट्ज़, स्वेन शेलियर (समीक्षा)|
| जापानी | कोकी तकेयमा, रियोतरो ऑकदा (समीक्षा)|
| कोरिअन| यौन्ग्जये जेओं, जेओंग्वों चो, जियौ हान, जियेऑन सुन्ग|
| रूसी | गल्ल मक्सिम, एउगेन मर्त्य्नोव, चलनोकोव व्लादिस्लाव (समीक्षा), ओप्री ईगोर (समीक्षा), टेरेशिन दिमित्री (समीक्षा)|
|स्पेनिश | मार्टिन मार्सिकनो, कार्लोस होलगुएरा|
|हिंदी | मुकेश शर्मा, कुंवर अतुल सिंह, रितेश कुमार, विक्रांत शाह, देवेंद्र कुमार सिन्हा, पराग दवे|
<br/>
यह दस्तावेज़ जिम मैनिको द्वारा लिखित OWASP एप्लीकेशन सिक्योरिटी वेरिफिकेशन स्टैंडर्ड के एक विशाख के रूप में शुरू हुआ।

## Sponsors

## प्रायोजक

While both the MASVS and the MSTG are created and maintained by the community on a voluntary basis, sometimes a little bit of outside help is required. We therefore thank our sponsors for providing the funds to be able to hire technical editors. Note that their sponsorship does not influence the content of the MASVS or MSTG in any way. The sponsorship packages are described on the [OWASP Project Wiki](https://www.owasp.org/index.php/OWASP_Mobile_Security_Testing_Guide#tab=Sponsorship_Packages "OWASP Mobile Security Testing Guide Sponsorship Packages").

हालांकि MASVS और MSTG दोनों को स्वैच्छिक आधार पर समुदाय द्वारा बनाया और बनाए रखा जाता है, कभी-कभी थोड़ी बहुत बाहरी मदद की आवश्यकता होती है। इसलिए हम तकनीकी प्रायोजकों को नियुक्त करने में सक्षम होने के लिए धन प्रदान करने के लिए अपने प्रायोजकों को धन्यवाद देते हैं। ध्यान दें कि उनके प्रायोजन किसी भी तरह से MASVS या MSTG की सामग्री को प्रभावित नहीं करते हैं। प्रायोजन पैकेज पर वर्णित हैं [OWASP Project Wiki](https://www.owasp.org/index.php/OWASP_Mobile_Security_Testing_Guide#tab=Sponsorship_Packages "OWASP मोबाइल सुरक्षा परीक्षण गाइड प्रायोजन पैकेज")।

### Honourable Benefactor

### माननीय उपकारी

[<img src="images/NowSecure_logo.png" title="NowSecure" width="200px" height="58px" />](https://www.nowsecure.com/ "NowSecure")

### Good Samaritan Benefactor

### अच्छा धार्मिक उपकारी

[<img src="images/Randorisec_logo.png" title="Randorisec" width="200px" height="58px" />](https://www.randorisec.fr/ "RandoriSec")

Next, we would like to thank the OWASP Bay Area Chapter for their sponsorship. Last, we would like to thank everybody that bought the book from Leanpub and sponsored us that way.

इसके बाद, हम उनके प्रायोजन के लिए OWASP बे एरिया चैप्टर को धन्यवाद देना चाहते हैं। अंत में, हम हर उस शख्स का शुक्रिया अदा करना चाहेंगे जिसने लीनपब से किताब खरीदी और हमें उस तरह से प्रायोजित किया।
