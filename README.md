# USPTO Checker

Checks the USPTO for the existence of their daily XML file at https://bulkdata.uspto.gov/data/trademark/dailyxml/applications/

### Setup

Install [Poetry](https://python-poetry.org/) for dependency management and virtual environment.

### Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to install the project dependencies:
    
```
poetry install
```
    
4. Initiate the virtual environment

```
poetry shell
```

    
### Usage

    
Run the script using the following command:
    
```
python check_uspto.py
```
    
This will check for the latest expected file. If you want a different date, pass the keyname as a parameter:

```
python check_uspto.py 231210
```


The script will check USPTO every 60 seconds and print the result. When the file is found, you'll be greeted with a sound alert.


### Dependencies

- Python >= 3.9
- requests
- beepy

### License

This project is licensed under the MIT License.

For more information, please refer to the documentation and the source code in the repository.
