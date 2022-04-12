# paper-QSLT
source codes of the QSLT mechansim


## For a randomness test, there are two steps:

1) generate random sequences.
    for QRNG, you can use getQRN.py
    for PRNG, you can use https://github.com/dj-on-github/djenrandom

2) evaluate the randomness by using NIST-800-22 tests.
    you can use command like: './sp800_22_tests.py xxx.bin', it will return a report of the test result. 
    the xxx.bin is a file of the generated random sequences.


This doctory is forked from https://github.com/dj-on-github/sp800_22_tests. 

You can evaluate the perfomance of QRNGs by using the following command: 
   ```python security_test_qrng.py```
and you can get results from a .txt file after the program finished.

You can evaluate the perfomance of PRNGs by using the following command: 
   ```python security_test_prng.py``` 
and you can get results from a .txt file after the program finished.

## For a ML model test, you can evaluate the perfomance by running the following commands:
* cancer dataset: ```python SVM_cancer.py```
* iris dataset: ```python SVM_iris.py```
* wine dataset: ```python SVM_wine.py```

pip library requirements:
```
qiskit==0.34.0
qiskit-aer==0.10.1
qiskit-ibmq-provider==0.18.3
qiskit-terra==0.19.1
qiskit-machine-learning==0.2.1
scikit-learn==1.0.2
scipy==1.7.3
numpy==1.21.5
```
