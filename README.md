# Simple blockchain

This is a simple blockchain implementation I build alongside this [tutorial](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46).

* It's quite simple and you can interact with it through http requests;
* It also has a simple consensus algo implemented on it.

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```
3. Install requirements  
```
$ pipenv install 
``` 

4. Run the server:
    * `$ pipenv run python blockchain.py` 
    * `$ pipenv run python blockchain.py -p 5001`
    * `$ pipenv run python blockchain.py --port 5002`
