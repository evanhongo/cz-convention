#!/usr/bin/env python
import os
import questionary


def main():
    answers = questionary.select(
        "What do you want to do?",
        choices=[
            "commit",
            "lint",
            "build",
            "release",
            "pipy deploy",
            "pipy test deploy",
            "install hooks",
        ],
    ).ask()  # returns value of selection
    if answers == "lint":
        os.system("black .")
    elif answers == "commit":
        os.system("black .")
        os.system("cz c")
    elif answers == "install hooks":
        os.system("pre-commit install")
        os.system("pre-commit install --hook-type commit-msg")
    elif answers == "build":
        os.system("rm dist/*")
        os.system("python setup.py sdist bdist_wheel")
    elif answers == "pipy deploy":
        os.system("python -m twine upload dist/*")
    elif answers == "pipy test deploy":
        os.system("python -m twine upload --repository testpypi dist/*")
    elif answers == "release":
        os.system("black .")
        os.system("cz bump -ch")


if __name__ == "__main__":
    main()
