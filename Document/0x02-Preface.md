# Preface

Welcome to the Mobile Application Security Verification Standard (MASVS) version [release number]. The MASVS is a community effort to establish a framework of security requirements needed to design, develop and test mobile apps on iOS and Android.

MASVS [release number] is a culmination of community effort and industry feedback. We expect this standard to evolve over time and welcome feedback from the community. The best way to get in contact with us is via the OWASP Mobile Project Slack channel:

https://owasp.slack.com/messages/project-mobile_omtg/details/

Accounts can be created at the following URL:

http://owasp.herokuapp.com/

## Introduction

Technological revolutions can happen quickly. Less than a decade ago, smartphones were clunky devices with little keyboards - expensive playthings for tech-savvy business users. Today, smartphones are an essential part of our lives. We've come to rely on them for information, navigation and communication, and they are ubiquitous both in business and in our social (public and private) lives.

Every new technology introduces new security risks, and keeping up with those changes is one of the main challenges the security industry faces. Defense is always a few steps behind. For example, the default reflex for many was to apply old ways of doing things: Smartphones are like small computers, and mobile apps are just like classic software, so surely the security requirements are similar? But it doesn't work like that. Smartphone operating systems are different from Desktop operating systems, and mobile apps are different from web apps. For example, the classical method of signature-based virus scanning doesn't make sense in modern mobile OS environments: Not only is it incompatible with the mobile app distribution model, it's also technically impossible due to sandboxing restrictions. Also, some vulnerability classes, such as buffer overflows and XSS issues, are less relevant in the context of run-of-the-mill mobile apps than in, say, Desktop apps and web applications (exceptions apply).

Over time, our industry has gotten a better grip on the mobile threat landscape. As it turns out, mobile security is all about data protection: Apps store our personal information, pictures, recordings, notes, account data, business information, location and much more. They act as clients that connect us to services we use on a daily basis, and as communications hubs that processes each and every message we exchange with others. Compromise a person's smartphone and you get unfiltered access to that person's life. When we consider that mobile devices are more readily lost or stolen and mobile malware is on the rise, the need for data protection becomes even more apparent.

A security standard for mobile apps must therefore focus on how mobile apps handle, store and protect sensitive information. Even though modern mobile operating systems like iOS and Android offer good APIs for secure data storage and communication, those have to be implemented and used correctly in order to be effective. Data storage, inter-app communication, proper usage of cryptographic APIs and secure network communication are only some of the aspects that require careful consideration.

An important question in need of industry consensus is how far exactly one should go in protecting sensitive data. For example, most of us would agree that a mobile app should verify the server certificate in a TLS exchange. But what about SSL certificate pinning? Does not doing it result in a vulnerability? Should it be a requirement if an app handles sensitive data, or is it maybe even counter-productive? What about locking the app or its session to the backend after a certain idle time? Do we need to encrypt data stored in SQLite databases, even though the OS sandboxes the app? What is appropriate for one app might be unrealistic for another. The MASVS is an attempt to standardize these requirements using verification levels for different use-cases.

The appearance of root malware and remote administration has made us aware that mobile operating systems themselves have exploitable flaws, so containerization strategies are increasingly used to afford additional protection to sensitive data. Additionally, in some cases it is desirable to prevent client-side tampering. This is where things get complicated. Hardware-backed security features such as the secure element (SE) and trusted execution environment (TEE) and OS-level containerization solutions such as Android for Work and Samsung Knox exist, but aren't consistently available across different devices. This can be somewhat mitigated by implementing software-based protection measures - but unfortunately, there are no standards or testing processes to verify these kinds of protections.

As a result, mobile app security testing reports are all over the place: For example, many testers report a lack of obfuscation or root detection in an Android app as security flaw. On the other hand, measures like string encryption, debugger detection or control flow obfuscation aren't considered mandatory. However, this binary way of looking at things doesn't make sense because resiliency is not a binary proposition: It depends on what one wants to achieve, and the particular client-side threats identified. Most importantly, software protections must never be used as a replacement for security controls.

The overall goal of the MASVS is to offer a baseline of mobile application security best practices, while also allowing for a defense-in-depth approach that adds additional protection mechanisms. The MASVS is meant to achieve the following:

- Provide requirements for software architects and developers seeking to develop secure mobile applications;
- Offer an industry standard that can be tested against in mobile app security reviews;
- Clarify the role of software protection mechanisms in mobile security and provide requirements to verify their effectiveness;
- Provide specific recommendations as to what level of security is recommended for different use-cases.

We are aware that 100% industry consensus is impossible to achieve. Nevertheless, we hope that the MASVS is useful in providing guidance throughout all phases of mobile app development and testing. As an open source standard, the MASVS will evolve over time, and we welcome any contributions and suggestions.
