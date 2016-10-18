# Preface

Welcome to the Mobile Application Security Verification Standard (MASVS) version 1.0. The MASVS is a community effort to establish a framework of security requirements and controls that focus on normalizing the functional and non-functional security controls required when designing, developing and testing mobile applications on iOS and Android.

MASVS [release number] is a culmination of community effort and industry feedback. We expect this standard to evolve over time and welcome feedback from the community. The best way to get in contact with us is via the OWASP Mobile Project Slack channel:

https://owasp.slack.com/messages/project-mobile_omtg/details/

Accounts can be created at the following URL:

http://owasp.herokuapp.com/


## Introduction

Technological revolutions can happen quickly. Less than a decade ago, smartphones were clunky devices with little keyboards - expensive playthings for tech-savvy business users. Today, smartphones are an essential part of our lives. We've come to rely on them for information, navigation and communication, and they are ubiquitous both in business and in our social (public and private) lives.

Every new technology introduces new security risks, and keeping up with those changes is one of the main challenges the security industry faces. Defense is always a few steps behind. For example, the default reflex for many was to apply old ways of doing things: Smartphones are like small computers, and mobile apps are like software, so surely the security requirements are similar? But it doesn't work like that. Smartphone operating systems are different from Desktop operating systems, and mobile apps are different from web apps: Virus scanners don't make sense on modern mobile OSes, and attackers rarely exploit buffer overflows and XSS vulnerabilities in mobile apps (rare exceptions exist).

Over time, our industry has gotten a better grip on the mobile threat landscape. As it turns out, mobile security is all about data protection: Apps store our personal information, pictures, notes, account data, business information, and much more. They act as clients that connect us to services we use on a daily basis, and as communications hubs that processes each and every message we exchange with others. Compromise a person's smartphone and you get unfiltered access to that person's life. When we consider that mobile devices are more readily lost or stolen and mobile malware is on the rise, the need for data protection becomes even more apparent.

A security standard for mobile apps must therefore focus on how mobile apps handle, store and protect sensitive information. Even though modern mobile operating systems like iOS and Android offer good APIs for secure data storage and communication, those have to be implemented and used correctly in order to be effective. Data storage, inter-app communication, proper usage of cryptographic APIs and secure network communication are only some of the aspects that require careful consideration.

An important question in need of industry consensus is how far exactly one should go in protecting sensitive data. For example, most of us would agree that a mobile app should verify the server certificate in a TLS exchange. But what about SSL pinning? Does not doing it result in a vulnerability? Should it be a requirement if an app handles sensitive data, or is it maybe even counter-productive? What about locking the app or it's session to the backend after a certain idle time? Do we need to encrypt data stored in SQLite databases, even though the OS sandboxes the app? What is appropriate for one app might be unrealistic for another. The MASVS is an attempt to standardize these requirements using verification levels for different use-cases.

Things become even more complicated when we start considering containerization and software protections. Some protective measures are widely assumed to be necessary - for example, many testers will report a lack of obfuscation or root detection in an Android app as security flaw. On the other hand, we don't usually consider string encryption, debugger detection or control flow obfuscation as mandatory. However, this binary way of looking at things doesn't make sense because software protection is not a binary proposition: The question is not whether an app can be reverse engineered or not, but rather how much has been done to make the process more difficult. Finding the right requirements and testing processes for software protections is a difficult problem unique to mobile security, where containerization and obfuscation is becoming quite common.

Finally, root malware and remote administration kits have made us aware that mobile operating systems themselves have exploitable flaws, so the case can be made that containerization, obfuscation and reactive defenses are valid strategies to add protective layers to mobile apps. Our goal is therefore to provide software protection requirements in the higher verification levels, as well as testing procedures for validating the effectiveness of the protections (which are documented in the Mobile Security Testing Guide).

The overall goal of the MASVS is to offer a baseline of mobile application security best practices, while also allowing for a defense-in-depth approach that adds additional protection mechanisms. The MASVS is meant to achieve the following:

- Provide requirements for software architects and developers seeking to develop secure mobile applications;
- Offer an industry standard to be used as a basis for mobile app security code review and testing methodologies;
- Clarify the role of software protection mechanisms in mobile security and provide requirements to verify their effectiveness;
- Provide specific recommendations as to what level of security is recommended for different use-cases.

We are aware that 100% industry consensus is impossible to achieve. Nevertheless, we hope that the MASVS is useful in providing guidance throughout all phases of mobile app development and testing. As an open source standard, the MASVS will evolve over time, and we welcome any contributions and suggestions.
