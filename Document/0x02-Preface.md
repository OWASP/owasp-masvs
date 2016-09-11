# Preface

Welcome to the Mobile Application Security Verification Standard (MASVS) version 1.0. The MASVS is a community-effort to establish a framework of security requirements and controls that focus on normalising the functional and non-functional security controls required when designing, developing and testing mobile applications on iOS and Android.

MASVS v1.0 is a culmination of community effort and industry feedback.

## Introduction

Technological revolutions happen quickly. Less than a decade ago, the smartphone as we know it didn't exist. Today, carrying a smartphone seems as essential to most people as wearing underwear (in fact, most sane people would rather leave the underwear at home). We've come to rely on these devices for information, navigation and communication, and they are ubiquitous both in business and private lives.

Every new technology introduces new security risks, and keeping up with those is one of the main challenges the security industry faces. In fact, we're always lagging a bit behind. Initially, we'll try to apply the old ways of doing things: Smartphones are like little computers, and mobile apps are like software, so surely the same security requirements apply? But it doesn't work like that: Smartphones are used differently from PCs, smartphone operating systems are different from Desktop operating systems, and mobile apps aren't web apps. Regardless what vendors want you to believe, mobile virus scanners don't make sense, and attackers are rarely exploiting buffer overflows or SQL injections in mobile apps. 

Talking of mobile app "penetration testing" is nonsense because there is nothing to penetrate. Instead, mobile apps are all about data protection. They store our personal information, notes, account data, business information, and much more. They act as clients that connect us to the services we use on a daily basis and as communications hub that processes every email and message we exchange with others. Compromise someone's smartphone and you get unfiltered access to that person's life.

A security standard for mobile apps must therefore focus mainly on how mobile apps handle, store and protect sensitive data. How do we ensure that it is as difficult as possible for adversaries to compromise the integrity and/or confidentiality of a mobile app? Even though modern mobile OSes offer reasonably good security by design, there's still a lot of things that can go wrong: Authentication, data storage, inter-app communcation, code quality and network communication all require careful consideration.

An important question in need of industry consensus is how far exactly one should go in protecting sensitive data. For example, all of us agree that a mobile app should verify the server certificate in a TLS exchange. But what about SSL pinning? Does not doing it result in a vulnerability? Should it be a requirement if an app handles more sensitive data, or is it maybe even counter-productive?

Things become even more confusing when we consider reverse engineering as an attack vector. Applying software protections is becoming increasingly common in mobile apps. Some methods are widely assumed to be useful - for example, many testers will report a lack of identifier renaming or root detection in an Android app as security flaw. On the other hand, we don't usually consider string encryption or control flow obfuscation as mandatory. This way of looking at things hardly makes sense because software protection is not a binary thing: The question is not whether an app can be reverse engineered or not, but rather how much has been done to make the process more difficult.

In designing the MASVS, we considered (...)
