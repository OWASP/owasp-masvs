# V1: Architecture, Design and Threat Modeling Requirements

## Control Objective

In a perfect world, security would be considered throughout all phases of development. In reality however, security is often only a consideration at a late stage in the SDLC. Besides the technical controls, the MASVS requires processes to be in place that ensure that the security has been explicitly addressed when planning the architecture of the mobile app, and that the functional and security roles of all components are known. Since most mobile applications act as clients to remote services, it must be ensured that appropriate security standards are also applied to those services - testing the mobile app in isolation is not sufficient.

The high level requirements are as follows:

- At MASVS-L1, components of the application are identified and have a reason for being in the app. All security controls are properly enforced on remote endpoints.
- At MASVS-L2, the architecture and threat model have been formally defined, and the code adheres to the architecture.
- With MASVS-R, the threat model extends to app-specific client-side attacks where the mobile operating system and/or end user are untrusted (e.g. stealing sensitive information that *must* be stored on the client, or cheating in an online game).

## Requirements

| # | Description | L1 | L2 | R |
| --- | --- | --- | --- | --- | --- |
| **1.1** | All app components are identified and known to be needed. | ✓ | ✓ | ✓ |
| **1.2** | All third party components used by the application, such as libraries and frameworks, are identified, and tested for known vulnerabilities. | ✓ | ✓ | ✓ |
| **1.3** | Security controls are never enforced only on the client-side, but on the respective remote endpoints. | ✓ | ✓ | ✓ |
| **1.4** | A high-level architecture for the mobile application and all connected remote services has been defined and security has been addressed in that architecture. |   | ✓ | ✓ |
| **1.5** | A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures. |   | ✓ | ✓ |
| **1.6** | All third party components have been assessed (associated risks) before being used or implemented. A process is in place to ensure that each time a security update for a third party component is published, the change is inspected and the risk evaluated. |   | ✓ | ✓ |
| **1.7** | All security controls (including libraries that call external security services) have a centralized implementation. |   | ✓ | ✓ |
| **1.8** | All application components are defined in terms of the business functions and/or security functions they provide. |   | ✓ | ✓ |
| **1.9** | All components that are not part of the application but that the application relies on to operate, are defined in terms of the functions, and/or security functions, they provide. |   | ✓ | ✓ |
| **1.10** | There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. |   | ✓ | ✓ |
| **1.11** | A process is in place to monitor first and third party app stores for copies of the app and for fake apps using a similar brand or name. |   | ✓ | ✓ |
| **1.12** | Application blacklisting (or whitelisting) is in place based on the application version & identifiers.  |   | ✓ | ✓ |
| **1.13** | To prevent cross-platform account compromise, authentication information for other channels is not reused in the mobile app. |   | ✓ | ✓ |
| **1.14** | The threat model extends to app-specific client-side attacks where the mobile operating system and/or end user are untrusted.  |   |   | ✓ |

## References

For more information, see also:

- OWASP Mobile Top 10: M10 - Extraneous Functionality
- OWASP Security Architecture cheat sheet: https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet
- OWASP Thread modelling: https://www.owasp.org/index.php/Application_Threat_Modeling
