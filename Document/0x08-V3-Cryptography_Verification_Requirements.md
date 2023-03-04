# MASVS-CRYPTO: Cryptography

## Description

Cryptography is essential for mobile apps because mobile devices are highly portable and can be easily lost or stolen. This means that an attacker who gains physical access to a device can potentially access all the sensitive data stored on it, including passwords, financial information, and personally identifiable information. Cryptography provides a means of protecting this sensitive data by encrypting it so that it cannot be easily read or accessed by an unauthorized user.

In addition, mobile apps often transmit sensitive data over unsecured networks, such as public Wi-Fi, which can increase the risk of interception by attackers. Cryptography can be used to encrypt this data and ensure its confidentiality and integrity during transmission.

The purpose of the controls in this category is to ensure that the verified app uses cryptography according to industry best practices, which are typically defined in external standards such as [NIST.SP.800-175B](https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final) and [NIST.SP.800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final). This category also focuses on the management of cryptographic keys throughout their lifecycle, including key generation, storage, and protection. Poor key management can compromise even the strongest cryptography, so it is crucial for developers to follow the recommended best practices to ensure the security of their users' sensitive data.

## Controls

| ID | Statement |
|----|-----------|
| MASVS-CRYPTO-1 | The app employs current strong cryptography and uses it according to industry best practices. |
| MASVS-CRYPTO-2 | The app performs key management according to industry best practices. |

## References

The OWASP Mobile Application Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- General: Mobile App Cryptography - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04g-Testing-Cryptography.md>
- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06e-Testing-Cryptography.md>
