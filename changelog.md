v1.2:
- Added " command: Enters/exits string mode which pushes characters as ASCII values
- Added { command: Pops a number off the stack and pushes each digit as an ASCII value
- Added > command: Skips to the final | or EOF
- Added < command: Skips to the first | or BOF
- Added ~ command: Reverses the stack
- Added ; command: Pops the bottom value from the stack and pushes it on top
- Reorganized code some

v1.1:
- Added ? command; pushes stack size to stack
- Added ^ command: waits for input, then pushes as an integer (0 if invalid)
- Added & command: waits for input, then pushes as ASCII values (character by character)
- Added _ command: exits program prematurely

v1.0:
- Initial release
