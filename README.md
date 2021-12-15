# TEAM: Graceful Fish

## Roster:
* Ishraq Mahid
* Grace Chen

## Project Description:
We are creating a capture the flag type of activity where users will be required to use SQL injection and other already-taught tools. For the presentation, we will be teaching how SQL works and how to use SQLmap/how it works. The activity will require users to connect to a virtual machine hosted on one of our personal computers.

## Daily Log:
12/14/2021
* Ishraq Mahid (in class): Worked on formatting repo + website app + slides for teaching SQL Database
* Grace Chen (in class): Worked on researching SQLmap and going through a tutorial for it + taking notes on how it works
* Grace Chen (at home): Successfully set up a virtual machine for use. Opened port on the machine and connected from another device and it works but not sure how to apply it to our project yet. Port seems to only be open when target machine is listening on that port (ex. with netcat).

## Haikus:
soon™

## Launch Codes:
Prerequisites:
    Python 3 is installed and necessary environment variables are setup properly.

Clone repo:
    <br>
    In the directory you want to have the code in, type into a terminal
    <br>
    ```
    $ git clone git@github.com:turtlelazy/cybersecurity_final.git
    ```

Create a virtual environment (unless you already have one):
    <br>
    A virtual environment can be created using the following line in a terminal
    <br>
    ```
    $ python3 -m venv ~/path/to/virtual/environment/directory
    ```
    <br>
    The virtual environment can then be activated by being in the right directory, then typing the following line in a terminal
    <br>
    ```
    $ source (name of virtual environment directory)/bin/activate
    ```
    <br>
    To then install the required packages, navigate to this repository, and enter in the following with the virtual environment activated:
    ```
    pip install -r requirements.txt
    ```

Launching the website app:
    <br>
    cd into app
    <br>
    activate the virtual environment
    <br>
    run ```python3 __init__.py```
    <br>
    Open the link given from the the terminal.

## Documents/Presentation
Link to planning document: https://docs.google.com/document/d/1Ha1vOAJRb35Ei32Rkq19hncYhVfalp1soGSrM-R59Ik/edit?usp=sharing
