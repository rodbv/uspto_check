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
python check.py
```
    
This will check for the latest expected file. If you want a different date, pass the keyname as a parameter:

```
python check.py --keyname 231210
```



The script will check USPTO every 60 seconds and print the result. 

![image](https://github.com/rodbv/uspto_check/assets/882489/c27798ff-af42-47e6-8c8b-89d04c0befc3)

When the file is found, it will check for the file size, since it's common for the USPTO to make empty files available. 

If the file is less than 1MB in size, you'll see this:




If the file size is OK, you'll be greeted with a sound alert.

![image](https://github.com/rodbv/uspto_check/assets/882489/f38b0fe0-4f51-4910-9b0e-2c2ac54ac3fc)

You can suppress the sound by passing the `--quiet` parameter.



### Pre-commit and Ruff Integration

This project also utilizes [pre-commit](https://pre-commit.com/) and [Ruff](https://github.com/astral-sh/ruff) for code quality and formatting checks. The pre-commit configuration file can be found in the project repository.


To set up pre-commit and integrate Ruff into your local development environment, follow these steps:


1. Navigate to the project directory.
2. Run the following command to install the pre-commit hooks:

```
pre-commit install
```

With pre-commit set up, Ruff will automatically check the formatting of Python files when you commit changes.

### License

This project is licensed under the MIT License.

For more information, please refer to the documentation and the source code in the repository.
