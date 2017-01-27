# The Mobile Application Security Verification Standard

The MASVS can be used to establish a level of confidence in the security of mobile apps. The requirements were developed with the following objectives in mind:

* Use as a metric - To provide a security standard against which existing mobile apps can be compared by developers and application owners;
* Use as guidance - To provide guidance during all phases of mobile app development and testing;
* Use during procurement - To provide a baseline for mobile app security verification.

## Mobile AppSec Model

The MASVS defines two strict *security verification levels (L1 and L2)*, as well a set of reverse engineering resiliency requirements (MASVS-R) that is "flexible", i.e. adaptable to an app-specific threat model. MASVS-L1 and MASVS-L2 contain generic security requirements and are recommended for all mobile apps (L1) and apps that handle highly sensitive data (L2). MASVS-R covers additional software protection controls that can be applied if preventing reverse engineering and/or tampering is a goal.

Fulfilling the requirements in MASVS-L1 results in a secure app that follows security best practices appropriately and doesn't suffer from common vulnerabilities. MASVS-L2 adds additional controls, resulting in an app that is resilient against more sophisticated attacks in a regular environment, assuming the security controls of the mobile operating system are assumed to be intact and the end user is not viewed as a potential adversary. Fulfilling all, or subsets of, the software protection requirements in MASVS-R helps impede specific client-side threats where the end user is malicious and/or the mobile OS is compromised.

**Note that software protections (MASVS-R) must never be used as a replacement for security controls. The controls listed in MASVR-R are intended to add threat-specific, additional protective controls to apps that also fulfill the MASVS requirements in MASVS L1 or L2.**

![Verification Levels](images/masvs-levels-new.jpg)

### Document Structure

The first part of the MASVS contains a description of the security model and available verification levels, followed by recommendations on how to use the standard in practice. The detailed security requirements, along with a mapping to the verification levels, are listed in the second part. The requirements have been grouped into eight categories (V1.. V8) based on technical objective / scope. The following nomenclature is used throughout the MASVS and MSTG:

- Requirement category: MASVS-Vx, e.g. MASVS-V2: Data Storage and Privacy
- Specific requirement: MASVS-Vx.y, e.g. MASVS-V2.2: "No sensitive data is written to application logs."  

### Verification Levels in Detail

#### MASVS-L1: Standard Security

A mobile app that achieves MASVS-L1 adheres to mobile application security best practices. It fulfills basic requirements in terms of code quality, handling of sensitive data, and interaction with the mobile environment. A testing process must be in place to verify the security controls. This level is appropriate for all mobile applications.

#### MASVS-L2: Defense-in-Depth

MASVS-L2 introduces advanced security controls that go beyond the standard requirements. To fulfill L2, a threat model must exist, and security must be an integral part of the app's architecture and design. Security must be verified using white-box testing. This level is appropriate for applications that handle sensitive data, such as mobile banking.

#### MASVS-R: Resiliency Against Reverse Engineering and Tampering

The app has state-of-the-art security, and is also resilient against specific, clearly defined client-side attacks, such as tampering, modding, or reverse engineering to extract sensitive code or data. Such an app either leverages hardware security features or sufficiently strong and verifiable software protection techniques. MASVS-R is applicable to apps that handle highly sensitive data and may serve as a means of protecting intellectual property or tamper-proofing an app.

### Recommended Use

Apps are verified against MASVS L1 or L2 depending on business risk. L1 is applicable to all mobile apps, while L2 is generally recommended for apps that handle more sensitive data and/or functionality. MASVS-R (or parts of it) can be applied *in addition* to proper security verification, to counter specific threats, such as repackaging or extraction of sensitive data.

In summary, The following verification types are available:

- MASVS L1
- MASVS L1+R
- MASVS L2
- MASVS L2+R

The different combinations reflect different grades of security and resiliency. The goal is to allow for flexibility: For example, a mobile game might not warrant adding MASVS-L2 measures such as 2-factor auth for usability reasons, but have a strong business need for tampering prevention.

#### Which Verification Type to Choose

Implementing the requirements of MASVS L2 increases security, while at the same time increasing cost of development and potentially worsening the end user experience (the classical trade-off). In general, L2 should be used for apps whenever it makes sense from a risk vs. cost perspective (i.e., where the potential loss caused by a compromise confidentiality or integrity is higher than the cost incurred by the addititional security controls). A risk assessment should be the first step before applying the MASVS.
