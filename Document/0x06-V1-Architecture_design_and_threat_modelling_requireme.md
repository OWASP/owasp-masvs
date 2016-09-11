# V1: Architecture, design and threat modelling requirements

## Control objective

todo

## Requirements

| # | Description | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **1.1** | Verify that all app components are identified and are known to be needed. | ✓ | ✓ | ✓ | ✓ |
| **1.2** | Verify that all third party components used by the app, such as libraries and frameworks, are identified. | ✓ | ✓ | ✓ | ✓ |
| **1.3** | Verify that all third party components are assessed and evaluated (associated risks) before being used or implemented. Whenever a security update is published of an implemented third party component, the change has to be inspected and the risk has to be evaluated. In the case a third party component causes the app itself to be vulnerable, the app has to be fixed as soon as possible. Therefore it is also recommended to limit the integration of third party components. |   | ✓ | ✓ | ✓ |
| **1.4** | Verify that a high-level architecture for the mobile app and its remote endpoints has been defined. |   | ✓ | ✓ | ✓ |
| **1.5** | Verify that all application components are defined in terms of the business functions and/or security functions they provide. |   |   | ✓ | ✓ |
| **1.6** | Verify that all components that are not part of the application but that the application relies on to operate are defined in terms of the functions, and/or security functions, they provide. |   |   | ✓ | ✓ |
| **1.7** | Verify that a threat model for the mobile app has been produced. |   |   | ✓ | ✓ |
| **1.8** | Verify all security controls (including libraries that call external security services) have a centralized implementation. |   | ✓ | ✓ | ✓ |
| **1.9** | Verify that there is no sensitive business logic, secret keys or other proprietary information in client side code. |   | ✓ | ✓ | ✓ |

## References

For more information, please see:

[TODO]
