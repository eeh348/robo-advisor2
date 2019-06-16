# robo-advisor
Shopping cart application for local grocery store

## Prerequisites

+ Anaconda 3.7
+ Python 3.7
+ Pip

## Installation

Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd robo_advisor
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

#Setup 

Create a python file called robo_advisor.py and a text file called requirements.txt. 

In the robo_advisor.py file, paste the following code:

# app/robo_advisor.py

```sh
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
```

In the requirements.txt, paste the follow text:

```sh
requests
python-dotenv
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install pytest

```

## Installation

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```
