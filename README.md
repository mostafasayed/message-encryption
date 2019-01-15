# Message Encryption

Encrypt messages using old fashion encryption way, Method start with asking user to input number of messages to be encrypted, message to be encrypted should contain caesar shifting indicator and method will do:
- Caesar shifting for all letter in message (convet number to words)
- Convert shifted letter to equivalent bit
- Convert bit to binary
- Encode binary by summing each element with surrounding element
- Convert encoded to binary
- Convert the binary to hexadecimal

**Problem designed by:** [Eng. Hossam Aly](https://github.com/hosamaly)

## Getting Started

Its very sample to start it no too much library needed, Just download the files and run it manual `python3 encrypt.py` or throw your IDE

### Prerequisites

You need to have virtual environment for python3 with num2words and pytest installed
```
pip3 install num2words
pip3 install pytest
```

## Running the tests

To run test cases you can install needed plug-in in your IDE (Pycharm already pytest runner are installed), Or use command `pytest`

## Versioning
1.0.0

## Authors

Mostafa Hanafy
