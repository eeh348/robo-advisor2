# robo-advisor
Robo advisor

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


## Installation

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install pytest

```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

Install the following modules

```sh
requests
datetime
json
csv
os
statistics
```

Install the following packages

```sh
from dotenv import load_dotenv
```

## API Requirements

Create .env file in the directory and create variable called ALPHAVANTAGE_API_KEY. Your program should read the API Key from this environment variable at run-time.

```sh
ALPHAVANTAGE_API_KEY="abc123"
```

To obtain an API key, go to https://www.alphavantage.co/support/#api-key
