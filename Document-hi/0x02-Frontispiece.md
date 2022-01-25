# मानक के बारे में

![OWASP Logo](images/OWASP_logo.png)

मोबाइल एप्लिकेशन सुरक्षा सत्यापन मानक (MASVS) 1.1 में आपका स्वागत है। MASVS आईओएस (iOS) और एंड्रॉइड पर सुरक्षित मोबाइल एप्लिकेशन को डिजाइन, विकसित और परीक्षण करने के लिए आवश्यक सुरक्षा आवश्यकताओं के ढांचे को स्थापित करने का एक सामुदायिक प्रयास है।

MASVS सामुदायिक प्रयास और उद्योग की प्रतिक्रिया के चरम बिंदु है। हम उम्मीद करते हैं कि यह मानक समय के साथ विकसित होगा और समुदाय से प्रतिक्रिया का स्वागत करेगा।

हमारे साथ संपर्क करने का सबसे अच्छा तरीका OWASP मोबाइल प्रोजेक्ट स्लैक चैनल है: <https://owasp.slack.com/messages/project-mobile_omtg/details/> .

निम्नलिखित URL पर खाते बनाए जा सकते हैं: [https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/](https://owasp.slack.com/join/shared_invite/zt-g398htpy-AZ40HOM1WUOZguJKbblqkw#/).

## कॉपीराइट और लाइसेंस

[![Creative Commons License](images/CC-license.png)](https://creativecommons.org/licenses/by-sa/4.0/)

कॉपीराइट © 2021 OWASP Foundation.यह काम एक [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) के तहत लाइसेंस प्राप्त है। किसी भी तरह के पुन: उपयोग या वितरण के लिए, आपको इस कार्य के लाइसेंस की शर्तों को दूसरों को स्पष्ट करना चाहिए।

<div style="page-break-after: always; visibility: hidden">
</div>

## आभार

|  प्रोजेक्ट लीड  |  लीड लेखक  |  योगदानकर्ता और समीक्षक  |
|  ---------  |  ---------  |  -------------------  |
| Sven Schleier and Carlos Holguera | Bernhard Mueller, Sven Schleier, Jeroen Willemsen and Carlos Holguera | Alexander Antukh, Mesheryakov Aleksey, Elderov Ali, Bachevsky Artem, Jeroen Beckers, Jon-Anthoney de Boer, Damien Clochard, Ben Cheney, Will Chilcutt, Stephen Corbiaux, Manuel Delgado, Ratchenko Denis, Ryan Dewhurst, @empty_jack, Ben Gardiner, Anton Glezman, Josh Grossman, Sjoerd Langkemper, Vinícius Henrique Marangoni, Martin Marsicano, Roberto Martelloni, @PierrickV, Julia Potapenko, Andrew Orobator, Mehrad Rafii, Javier Ruiz, Abhinav Sejpal, Stefaan Seys, Yogesh Sharma, Prabhant Singh, Nikhil Soni, Anant Shrivastava, Francesco Stillavato, Abdessamad Temmar, Pauchard Thomas, Lukasz Wierzbicki |
<br/>

| भाषा  | अनुवादक और समीक्षक |
| --- | ------------------  |
| ब्राजिलियन पुर्तगाली | Mateus Polastro, Humberto Junior, Rodrigo Araujo, Maurício Ariza, Fernando Galves |
| चीनी (पारंपरिक)| पीटर ची, और लेक्स चिएन, हेनरी हू, लियो वांग|
| चीनी (सरलीकृत)| बॉब पेंग, हेरोल्ड ज़ैंग, जैक एस|
| फ्रेंच | रोमुआल्ड स्ज़ुडलारेक, एबदर्रहमान आफ़ताही, क्रिश्चियन डोंग (समीक्षा)|
| जर्मन | रोक्को ग्रिट्ज़, स्वेन शेलियर (समीक्षा)|
| जापानी | कोकी तकेयमा, रियोतरो ऑकदा (समीक्षा)|
| कोरिअन| यौन्ग्जये जेओं, जेओंग्वों चो, जियौ हान, जियेऑन सुन्ग|
| रूसी | गल्ल मक्सिम, एउगेन मर्त्य्नोव, चलनोकोव व्लादिस्लाव (समीक्षा), ओप्री ईगोर (समीक्षा), टेरेशिन दिमित्री (समीक्षा)|
|स्पेनिश | मार्टिन मार्सिकनो, कार्लोस होलगुएरा|
| पुर्तगाली | Ana Filipa Mota, Fernando Nogueira, Filipa Gomes, Luis Fontes, Sónia Dias|
| फ़ारसी | Hamed Salimian, Ramin Atefinia, Dorna Azhirak, Bardiya Akbari, Mahsa Omidvar, Alireza Mazhari, Milad Khoshdel |
|हिंदी | मुकेश शर्मा, कुंवर अतुल सिंह, रितेश कुमार, विक्रांत शाह, देवेंद्र कुमार सिन्हा, पराग दवे|
<br/>
यह दस्तावेज़ जिम मैनिको द्वारा लिखित OWASP एप्लीकेशन सिक्योरिटी वेरिफिकेशन स्टैंडर्ड के एक विशाख के रूप में शुरू हुआ।

## प्रायोजक

हालांकि MASVS और MSTG दोनों को स्वैच्छिक आधार पर समुदाय द्वारा बनाया और बनाए रखा जाता है, कभी-कभी थोड़ी बहुत बाहरी मदद की आवश्यकता होती है। इसलिए हम तकनीकी प्रायोजकों को नियुक्त करने में सक्षम होने के लिए धन प्रदान करने के लिए अपने प्रायोजकों को धन्यवाद देते हैं। ध्यान दें कि उनके प्रायोजन किसी भी तरह से MASVS या MSTG की सामग्री को प्रभावित नहीं करते हैं। प्रायोजन पैकेज पर वर्णित हैं [OWASP Project Wiki](https://owasp.org/www-project-mobile-security-testing-guide/#div-sponsorship "OWASP मोबाइल सुरक्षा परीक्षण गाइड प्रायोजन पैकेज")।

### God Mode

![OWASP MSTG](images/Donators/NowSecure_logo.png) \

[OWASP Bay Area Chapter](https://twitter.com/OWASPBayArea?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor "Twitter Bay Area")

#### Honorable Benefactor

![OWASP MSTG](images/Donators/SEC_Consult_logo.png) \

![OWASP MSTG](images/Donators/ZIMPERIUM_logo.png) \

#### Good Samaritan

![OWASP MSTG](images/Donators/Randorisec_logo.png) \

इसके बाद, हम उनके प्रायोजन के लिए OWASP बे एरिया चैप्टर को धन्यवाद देना चाहते हैं। अंत में, हम हर उस शख्स का शुक्रिया अदा करना चाहेंगे जिसने लीनपब ([Leanpub](https://leanpub.com/mobile-security-testing-guide)) से किताब खरीदी और हमें उस तरह से प्रायोजित किया।
