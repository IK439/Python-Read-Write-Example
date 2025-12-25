import csv
import json

# Initialize an empty list to store compromised users
users_compromised = []

# Attempt to read the passwords CSV file
# Extract the 'Username' column from each row and store in users_compromised list
try:
    with open('passwords.csv', newline='') as password_file:
        password_csv = csv.DictReader(password_file)
        users_compromised = [row['Username'] for row in password_csv]

# Handle different error types
except FileNotFoundError:
    print("Error: 'passwords.csv' file not found.")
except PermissionError:
    print("Error: Permission denied while reading 'passwords.csv'.")
except Exception as e:
    print(f"An unexpected error occurred while reading 'passwords.csv': {e}")

# Attempt to write the compromised usernames to a text file
try:
    with open('users_compromised.txt', 'w') as users_compromised_file:
        for user in users_compromised:
            users_compromised_file.write(user + '\n')

# Handle different error types
except PermissionError:
    print("Error: Permission denied while writing 'users_compromised.txt'.")
except Exception as e:
    print(f"An unexpected error occurred while writing 'users_compromised.txt': {e}")

# Attempt to write mission status to a JSON file
try:
    with open('mission_status.json', 'w') as mission_status:
        mission_status_dict = {
            'recipient': 'The Boss',
            'message': 'Mission Successful'
        }
        json.dump(mission_status_dict, mission_status)  # Serialize dictionary to JSON and write to file

# Handle different error types
except PermissionError:
    print("Error: Permission denied while writing 'mission_status.json'.")
except Exception as e:
    print(f"An unexpected error occurred while writing 'mission_status.json': {e}")

# Attempt to write ASCII art to a new passwords CSV file
try:
    with open('new_passwords.csv', 'w') as new_passwords_obj:
        ik439_sig = """                              
██    ██  ██████  ██    ██                          
 ██  ██  ██    ██ ██    ██                          
  ████   ██    ██ ██    ██                          
   ██    ██    ██ ██    ██                          
   ██     ██████   ██████                           
                                                    
                                                    
 ██████   ██████  ████████                          
██       ██    ██    ██                             
██   ███ ██    ██    ██                             
██    ██ ██    ██    ██                             
 ██████   ██████     ██                             
                                                    
                                                    
██   ██  █████   ██████ ██   ██ ███████ ██████      
██   ██ ██   ██ ██      ██  ██  ██      ██   ██     
███████ ███████ ██      █████   █████   ██   ██     
██   ██ ██   ██ ██      ██  ██  ██      ██   ██     
██   ██ ██   ██  ██████ ██   ██ ███████ ██████      
                                                    
                                                    
          ██ ██   ██ ██   ██ ██████   █████         
          ██ ██  ██  ██   ██      ██ ██   ██        
█████     ██ █████   ███████  █████   ██████        
          ██ ██  ██       ██      ██      ██        
          ██ ██   ██      ██ ██████   █████                
"""
        new_passwords_obj.write(ik439_sig)

# Handle different error types
except PermissionError:
    print("Error: Permission denied while writing 'new_passwords.csv'.")
except Exception as e:
    print(f"An unexpected error occurred while writing 'new_passwords.csv': {e}")