# Cookiecutter PKI

_A structured, standardized project structure for creating PKI infrastructure._

### Requirements
----------------
- Python 2.7 or 3.5
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

### Project Creation
--------------------

    cookiecutter https://github.com/Jberlinsky/cookiecutter-pki

### Directory Structure
-----------------------

The directory structure of the resulting project looks like:

```
├── Makefile
└── ca
    ├── client
    │   ├── certs
    │   ├── crl
    │   ├── csr
    │   ├── newcerts
    │   ├── pfx
    │   └── private
    ├── intermediate
    │   ├── certs
    │   ├── crl
    │   ├── crlnumber
    │   ├── csr
    │   ├── database
    │   ├── newcerts
    │   ├── private
    │   └── serial
    ├── openssl.cnf
    ├── root
    │   ├── certs
    │   ├── crl
    │   ├── crlnumber
    │   ├── csr
    │   ├── database
    │   ├── newcerts
    │   ├── private
    │   └── serial
    └── server
        ├── certs
        ├── crl
        ├── csr
        ├── newcerts
        ├── pfx
        └── private
```

### Running tests
-----------------

    py.test tests

### Contributing
----------------

Contributions are welcome; please submit a pull request.
