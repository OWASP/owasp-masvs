# V8: Resiliency Against Reverse Engineering Requirements

## Control objective

... (todo) ...

## Requirements

| # | Verified | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| **9.12** | Verify that a form of source code obfuscation is implemented, to increase the cost of reverse engineering attacks on protocols or application components. On Android this could be proguard or dexguard. On iOS some implementations exist, but there is less need because of the increased complexity (higher cost) of reverse engineering. |   |   | ✓ | ✓ |
| **9.13** | Verify that anti-debugging and anti-emulator functionalities are implemented, to increase the cost of reverse engineering attacks on the application as well as protecting runtime data streams |   |   |   | ✓ |
| **9.13** | Verify that the application doesn't implement easy logic testing, especially for enabling or disabling security specific functionalities. By simply writing to these variables in memory, the application's logic could be tampered with. Furthermore, the possibility of reading these variables could help an attacker understanding the application's logic while reverse engineering it |   |   |   | ✓ |


## References

... (todo) ...
