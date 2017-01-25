# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

In a perfect world, security would be considered throughout all phases of development. In reality however, security is often only a consideration at a late stage in the SDLC. Besides the technical controls, the MASVS requires processes to be in place that ensure that the security has been explicitly addressed when planning the architecture of the mobile app, and that the functional and security roles of all components are known. Since most mobile applications act as clients to remote services, it must be ensured that appropriate security standards are also applied to those services - testing the mobile app in isolation is not sufficient.

The high level requirements are as follows:

- At MASVS-L1, components of the application are identified and have a reason for being in the app. All security controls are properly enforced on remote endpoints.
- At MASVS-L2, the architecture and threat model have been formally defined, and the code adheres to the architecture.

## Security Verification Requirements

| # | Description | L1 | L2 |
| --- | --- | --- | --- |
| **1.1** | All app components are identified and known to be needed. | ✓ | ✓ |
| **1.2** | All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities. | ✓ | ✓ |
| **1.3** | Security controls are never enforced only on the client side, but on the respective remote endpoints. | ✓ | ✓ |
| **1.4** | A high-level architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture. | ✓ | ✓ |
| **1.5** | Data considered sensitive in the context of the mobile app is clearly identified. | ✓ | ✓ |
| **1.6** | All app components are defined in terms of the business functions and/or security functions they provide. |   | ✓ |
| **1.7** | A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures. |   | ✓ |
| **1.8** | All third party components have been assessed (associated risks) before being used or implemented. A process is in place to ensure that each time a security update for a third party component is published, the change is inspected and the risk evaluated. |   | ✓ |
| **1.9** | All security controls have a centralized implementation. |   | ✓ |
| **1.10** | All components that are not part of the application but that the application relies on to operate, are clearly identified and the security implications of using those components are known. |   | ✓ |
| **1.11** | There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 800-57. |   | ✓ |
| **1.12** | Remote endoints verify that connecting clients use the current version of the mobile app. |   | ✓ |
| **1.13** | Security testing is performed as part of the development lifecycle. If some or all of the testing is automated, the configuration of the testing tools must be tailored to the specific app. |   | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M10 - Extraneous Functionality
- OWASP Security Architecture cheat sheet: https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet
- OWASP Thread modelling: https://www.owasp.org/index.php/Application_Threat_Modeling
