# Python-Read-Write-Example

This repository contains a Python script that demonstrates reading from and writing to files. The script performs the following tasks:

## Features

1. **Read compromised usernames from a CSV file**

   * Reads `passwords.csv` using `csv.DictReader`.
   * Extracts the `Username` column and stores it in a list.
   * Handles `FileNotFoundError`, `PermissionError`, and other exceptions.

2. **Write compromised usernames to a text file**

   * Writes each username to `users_compromised.txt`, one per line.
   * Handles file permission errors and other exceptions.

3. **Write mission status to a JSON file**

   * Creates `mission_status.json` containing the recipient and message.
   * Uses `json.dump()` to serialize the dictionary.
   * Handles exceptions during file writing.

4. **Write ASCII art to a new passwords CSV file**

   * Writes a predefined ASCII signature to `new_passwords.csv`.
   * Handles exceptions during file writing.

## Usage

1. Ensure `passwords.csv` exists and contains a `Username` column.
2. Run the script with Python 3:

   ```bash
   python script_name.py
   ```
3. Check the following output files:

   * `users_compromised.txt` – list of usernames
   * `mission_status.json` – mission status information
   * `new_passwords.csv` – contains ASCII art signature

## Exception Handling

* The script handles missing files, permission errors, and unexpected exceptions for robust execution.
* Errors are printed to the console for easy debugging.

## Dependencies

* Python 3.x
* `csv` module (built-in)
* `json` module (built-in)

## Notes

* Ensure proper permissions for reading and writing files.
* The script assumes `Username` column exists in `passwords.csv`.
* ASCII art is written in plain text; some terminals may not render it correctly.
