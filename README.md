First install `pyjwt` via:

```shell
pip install pyjwt
```

and ensure you have at least Python 3.5.

Then generate keys by running:

```shell
bash keygen.sh <keyname>
```

where `<keyname>` has `.key` at the end of it, like `test.key`. This creates a private and public key in the same directory. 

Then run:

```shell
python pyjwt_example.py <private keyname> <public keyname>
```

It will print the JWT, the original message, and the decoded message.
