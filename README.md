## Enc2File module.

----
#### What is Enc2File?
Small module to easily encrypt and decrypt strings from stdin and files using cryptography's Fernet recipe.

Check [cryptography docs](https://cryptography.io/en/latest/fernet/#) for details on the ecryption used.

----
#### Requirements.
- Python 3.6.
- Cryptography 2.1.4.

----
#### Installation.
1. git clone https://github.com/Asta1986/enc2file.git
2. cd enc2file
3. pip install .

**To uninstall it:** pip uninstall enc2file

----
#### Usage
Most importantly, to decrypt a string the encryption key and encoding have to be the same as those used to encrypt it.
UTF-8 is used by default.

**Example 1. Store an encrypted string in one file and the encryption key used in a different one.**


    import enc2file
    
    enc = enc2file.Enc2File()
    enc.enc2file('a_test_string', '/dir/msg.file')
    enc.key_to_file('/dir/key.file')
    
**Example 2. Read an encrypted string from file and print it.**


    import enc2file
    
    enc = enc2file.Enc2File()
    enc.key_from_file('/dir/key.file')
    decypted_string = enc.decrypt_from_file('/dir/msg.file')
    print(decypted_string)
