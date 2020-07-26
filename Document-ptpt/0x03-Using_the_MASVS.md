# The Mobile Application Security Verification Standard

The MASVS can be used to establish a level of confidence in the security of mobile apps. The requirements were developed with the following objectives in mind:

- Use as a metric - To provide a security standard against which existing mobile apps can be compared by developers and application owners;
- Use as guidance - To provide guidance during all phases of mobile app development and testing;
- Use during procurement - To provide a baseline for mobile app security verification.

## Mobile AppSec Model

The MASVS defines two security verification levels (MASVS-L1 and MASVS-L2), as well as a set of reverse engineering resiliency requirements (MASVS-R). MASVS-L1 contains generic security requirements that are recommended for all mobile apps, while MASVS-L2 should be applied to apps handling highly sensitive data. MASVS-R covers additional protective controls that can be applied if preventing client-side threats is a design goal.

Fulfilling the requirements in MASVS-L1 results in a secure app that follows security best practices and doesn't suffer from common vulnerabilities. MASVS-L2 adds additional defense-in-depth controls such as SSL pinning, resulting in an app that is resilient against more sophisticated attacks - assuming the security controls of the mobile operating system are intact and the end user is not viewed as a potential adversary. Fulfilling all, or subsets of, the software protection requirements in MASVS-R helps impede specific client-side threats where the end user is malicious and/or the mobile OS is compromised.

**I: Although we recommend implementing MASVS-L1 controls in every app, implementing a control or not should ultimately be a risk-based decision, which is taken/communicated with the business owners.**

**II: Note that the software protection controls listed in MASVS-R and described in the OWASP Mobile Security Testing Guide can ultimately be bypassed and must never be used as a replacement for security controls. Instead, they are intended to add additional threat-specific, protective controls to apps that also fulfill the MASVS requirements in MASVS-L1 or MASVS-L2.**

<img src="images/masvs-levels-new.jpg" title="Verification Levels" width="600px" height="253px" />

### Document Structure

The first part of the MASVS contains a description of the security model and available verification levels, followed by recommendations on how to use the standard in practice. The detailed security requirements, along with a mapping to the verification levels, are listed in the second part. The requirements have been grouped into eight categories (V1 to V8) based on technical objective / scope. The following nomenclature is used throughout the MASVS and MSTG:

- *Requirement category:* MASVS-Vx, e.g. MASVS-V2: Data Storage and Privacy
- *Requirement:* MASVS-Vx.y, e.g. MASVS-V2.2: "No sensitive data is written to application logs."  

### Verification Levels in Detail

#### MASVS-L1: Standard Security

A mobile app that achieves MASVS-L1 adheres to mobile application security best practices. It fulfills basic requirements in terms of code quality, handling of sensitive data, and interaction with the mobile environment. A testing process must be in place to verify the security controls. This level is appropriate for all mobile applications.

#### MASVS-L2: Defense-in-Depth

MASVS-L2 introduces advanced security controls that go beyond the standard requirements. To fulfill MASVS-L2, a threat model must exist, and security must be an integral part of the app's architecture and design. Based on the threat model, the right MASVS-L2 controls should have been selected and implemented successfully. This level is appropriate for apps that handle highly sensitive data, such as mobile banking apps.

#### MASVS-R: Resiliency Against Reverse Engineering and Tampering

The app has state-of-the-art security, and is also resilient against specific, clearly defined client-side attacks, such as tampering, modding, or reverse engineering to extract sensitive code or data. Such an app either leverages hardware security features or sufficiently strong and verifiable software protection techniques. MASVS-R is applicable to apps that handle highly sensitive data and may serve as a means of protecting intellectual property or tamper-proofing an app.

### Recommended Use

Apps can be verified against MASVS L1 or L2 based on prior risk assessment and overall level of security required. L1 is applicable to all mobile apps, while L2 is generally recommended for apps that handle more sensitive data and/or functionality. MASVS-R (or parts of it) can be applied to verify resiliency against specific threats, such as repackaging or extraction of sensitive data, *in addition* to proper security verification.

In summary, the following verification types are available:

- MASVS-L1
- MASVS-L1+R
- MASVS-L2
- MASVS-L2+R

The different combinations reflect different grades of security and resiliency. The goal is to allow for flexibility: For example, a mobile game might not warrant adding MASVS-L2 security controls such as 2-factor authentication for usability reasons, but have a strong business need for tamper prevention.

#### Which Verification Type to Choose

Implementing the requirements of MASVS L2 increases security, while at the same time increasing cost of development and potentially worsening the end user experience (the classical trade-off). In general, L2 should be used for apps whenever it makes sense from a risk vs. cost perspective (i.e., where the potential loss caused by a compromise of confidentiality or integrity is higher than the cost incurred by the additional security controls). A risk assessment should be the first step before applying the MASVS.

##### Examples

###### MASVS-L1

- All mobile apps. MASVS-L1 lists security best practices that can be followed with a reasonable impact on development cost and user experience. Apply the requirements in MASVS-L1 for any app that don't qualify for one of the higher levels.

<!-- \pagebreak -->

###### MASVS-L2

- Health-Care Industry: Mobile apps that store personally identifiable information that can be used for identity theft, fraudulent payments, or a variety of fraud schemes. For the US healthcare sector, compliance considerations include the Health Insurance Portability and Accountability Act (HIPAA) Privacy, Security, Breach Notification Rules and Patient Safety Rule.

- Financial Industry: Apps that enable access to highly sensitive information like credit card numbers, personal information, or allow the user to move funds. These apps warrant additional security controls to prevent fraud. Financial apps need to ensure compliance to the Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Act and Sarbanes-Oxley Act (SOX).

###### MASVS L1+R

- Mobile apps where Intellectual Property (IP) protection is a business goal. The resiliency controls listed in MASVS-R can be used to increase the effort needed to obtain the original source code and to impede tampering / cracking.

- Gaming Industry: Games with an essential need to prevent modding and cheating, such as competitive online games. Cheating is an important issue in online games, as a large amount of cheaters leads to a disgruntled player base and can ultimately cause a game to fail. MASVS-R provides basic anti-tampering controls to help increase the effort for cheaters.

###### MASVS L2+R

- Financial Industry: Online banking apps that allow the user to move funds, where techniques such as code injection and instrumentation on compromised devices pose a risk. In this case, controls from MASVS-R can be used to impede tampering, raising the bar for malware authors.

- All mobile apps that, by design, need to store sensitive data on the mobile device, and at the same time must support a wide range of devices and operating system versions. In this case, resiliency controls can be used as a defense-in-depth measure to increase the effort for attackers aiming to extract the sensitive data.

- Apps with in-app purchases should ideally use server-side and MASVS-L2 controls to protect paid content. However, there may be cases where there is no possibility to use server-side protection. In those cases, MASVS-R controls should be additionally applied in order to increase the reversing and/or tampering effort.
