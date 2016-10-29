# V1: Architecture, design and threat modelling requirements

## Control objective

In a perfect world, security would be considered throughout all phases of development. In reality however, security is often only a consideration at a late stage in the SDLC. Besides the technical controls, the MASVS requires processes to be in place that ensure that the security has been explicitly addressed when planning the architecture of the mobile app, and that the functional and security roles of all components are known. Since most mobile applications act as clients to remote services, it must be ensured that appropriate security standards are also applied to those services - testing the mobile app in isolation is not sufficient.

The high level requirements are as follows:

- At level 1, components of the application are identified and have a reason for being in the app
- At level 2 and higher, the architecture has been defined and the code adheres to the architecture. Additionally, a threat model exists that identifies potential threats.

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **1.1** | Verify that all app components are identified and are known to be needed. | ✓ | ✓ | ✓ | ✓ |
| **1.2** | Verify that all third party components used by the application, such as libraries and frameworks, are identified, and tested for known vulnerabilities. | ✓ | ✓ | ✓ | ✓ |
| **1.3** | Verify that a high-level architecture for the mobile application and any connected remote services has been defined and that security has been addressed in that architecture. |   | ✓ | ✓ | ✓ |
| **1.4** | Verify that a threat model for the mobile app and any connected remote services has been produced to identify potential threats and countermeasures to work against them. |   | ✓ | ✓ | ✓ |
| **1.5** | Verify that all third party components are assessed and evaluated (associated risks) before being used or implemented. Whenever a security update is published of an implemented third party component, the change has to be inspected and the risk has to be evaluated. |   | ✓ | ✓ | ✓ |
| **1.6** | Verify that all security controls (including libraries that call external security services) have a centralized implementation. |   | ✓ | ✓ | ✓ |
| **1.7** | Verify that all application components are defined in terms of the business functions and/or security functions they provide. |   | ✓ | ✓ | ✓ |
| **1.8** | Verify that all components that are not part of the application but that the application relies on to operate, are defined in terms of the functions, and/or security functions, they provide. |   | ✓ | ✓ | ✓ |
| **1.9** | If the app uses cryptography, verify that there is an explicit policy for how cryptographic keys are managed (e.g. generated, distributed, revoked, and expired), and verify that the key lifecycle is properly enforced. |   | ✓ | ✓ | ✓ |
| **1.10** | Verify that security controls are not only enforced on an app, but on the respective endpoints as well. |   | ✓ | ✓ | ✓ |
| **1.11** | Verify that there is a process in place to monitor first and third party app stores for copies of the app and for fake apps using a similar brand or name. |   |  | ✓ | ✓ |
| **1.12** | Verify that application blacklisting (or whitelisting) is in place based on the application version & identifiers.  |   |  | ✓ | ✓ |
| **1.13** | Verify that authentication information for other channels is not reused in the mobile implementation to prevent cross-platform account compromise. |   |  | ✓ | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M10 - Extraneous Functionality
- OWASP Security Architecture cheat sheet: https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet
- OWASP Thread modelling: https://www.owasp.org/index.php/Application_Threat_Modeling
