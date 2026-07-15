# MASVS-RESILIENCE-1

## Control

The app validates the integrity of the platform.

## Description

Running on a compromised platform that can be very dangerous for the user, as this may disable certain security features, putting the data of the user at risk. A compromised platform can disable certain security features (e.g. secure storage, biometrics, sandboxing, etc.). This control tries to validate that the OS has not been compromised and its security features can thus be trusted.

On the other hand, these controls are arguably the responsibility of the platforms. Moreover, The user may have legitimate reasons to run the application on an alternative platform, which make actually be more secure than the blessed platform and it may not be possible for the application to make the distinction between a compromised platform and an alternative platform chosen by the user. Refusing to execute on alternative platforms can therefore have a negative impact on security, sovereignty and reinforce anti-competitive practices by platform vendors. Therefore, while it may be reasonable to warn the user if the application has reasons to believe that some security features may be disabled or that the platform may be compromised, locking the user out of the application is usually not legitimate.
