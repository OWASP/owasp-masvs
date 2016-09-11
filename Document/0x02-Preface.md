# Preface

Welcome to the Mobile Application Security Verification Standard (MASVS) version 1.0. The MASVS is a community-effort to establish a framework of security requirements and controls that focus on normalising the functional and non-functional security controls required when designing, developing and testing mobile applications on iOS and Android.

MASVS v1.0 is a culmination of community effort and industry feedback.

## Introduction

Technological revolutions can happen quickly. Less than a decade ago, the smartphone as we know it didn't exist. Today, it is hard to imagine life without them. We've come to rely on these devices for information, navigation and communication, and they are ubiquitous both in business and private lives.

Every new technology introduces new security risks, and keeping up with those changes is one of our main challenges as an industry. In fact, we're always lagging a bit behind. The initial reflex is to use the old ways of doing things: Smartphones are like little computers, and mobile apps are like software, so surely security requirements are similar? But it doesn't work like that. Smartphone operating systems are different from Desktop operating systems, and mobile apps are different from web apps: Virus scanners don't make sense on modern mobile OSes, and attackers rarely "penetrate" mobile apps using buffer overflows and SQL injection vulnerabilities.

Over time, we have gotten a better grip on the mobile threat landscape. As it turns out, mobile security is all about data protection: Apps store our personal information, notes, account data, business information, and much more. They act as clients that connect us to services we use on a daily basis, and as communications hubs that processes each and every message we exchange with others. Compromise a person's smartphone and you get unfiltered access to that person's life. Considering that mobile devices are more readily lost or stolen and mobile malware is on the rise, the need for data protection becomes even more apparent.

A security standard for mobile apps must therefore focus on how mobile apps handle, store and protect sensitive information. Even though operating systems like iOS and Android have been designed with security in mind, there's still a lot of things app developers can do wrong: Authentication, session management, data storage, inter-app communication, network communication are only some of the aspects that require careful consideration. 

An important question in need of industry consensus is how far exactly one should go in protecting sensitive data. For example, most of us would agree that a mobile app should verify the server certificate in a TLS exchange. But what about SSL pinning? Does not doing it result in a vulnerability? Should it be a requirement if an app handles more sensitive data, or is it maybe even counter-productive?

Things become even more controversial when we consider reverse engineering as an attack vector. Applying software protections is becoming increasingly common in mobile apps. Some methods are widely assumed to be useful - for example, many testers will report a lack of identifier renaming or root detection in an Android app as security flaw. On the other hand, we don't usually consider string encryption or control flow obfuscation as mandatory. This binary way of looking at things hardly makes sense because software protection is not a binary proposition: The question is not whether an app can be reverse engineered or not, but rather how much has been done to make the process more difficult.

In designing the MASVS, we attempted to consider all of the above points. The goal was to offer a baseline security standard that lists all the best practices that have emerged in the industry, while also allowing for an defense-in-depth approach that adds additional protection mechanisms in cases where highly sensitive data is handled. 

1. Provide requirements for software architects and developers seeking to develop secure mobile applications;
2. Offer an industry standard to be used as a basis for mobile app security code review and testing methodologies;
3. Clarify the role of software protection mechanisms in mobile security and provide requirements to verify their effectiveness;
4. Provide specific recommendations as to what level of security is recommended for different use-cases.

We are aware that 100% industry consensus is impossible to achieve - as is 100% security. Nevertheless, we hope that the MASVS is useful in providing guidance throughout all phases of mobile app development and testing. As an open source standard, the MASVS will evolve over time, and any contributions and suggestions are welcome.
