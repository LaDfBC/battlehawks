from selenium import webdriver
import time

'''
    Hey Alex, I'm gonna be insane about comments on this so you know what's happening.
    
    First up, we're making the main function that'll be called to submit an entry
'''
def submit(email, first_name, last_name, phone_number, zip):
    # This is using Selenium, which is a Python library built to fake interactions with webpages
    driver = webdriver.Firefox()
    driver.get('https://www.xfl.com/en-US/teams/st-louis/battlehawks-sweepstakes/battlehawk-for-a-day-sweepstakes')

    # Each of these "fills in" the proper element
    email_element = driver.find_element_by_id('email')
    driver.execute_script("arguments[0].value = arguments[1]", email_element, email)

    fname_element = driver.find_element_by_id('email')
    driver.execute_script("arguments[0].value = arguments[1]", fname_element, first_name)

    lname_element = driver.find_element_by_id('email')
    driver.execute_script("arguments[0].value = arguments[1]", lname_element, last_name)

    phone_element = driver.find_element_by_id('email')
    driver.execute_script("arguments[0].value = arguments[1]", phone_element, phone_number)

    zip_element = driver.find_element_by_id('email')
    driver.execute_script("arguments[0].value = arguments[1]", zip_element, zip)

    # This hits the initial submit button...
    button = driver.find_element_by_class_name("s-form__submit s-form__submit--undefined")
    button.click()

    # ... and this gets past the Captcha
    driver.find_element_by_xpath("//span[@id='recaptcha-anchor']").click()

'''
    "Main" is the industry standard name for a function that is called to start off the run of a program.
    This one controls the loop that submits an entry, waits 31 seconds, then repeats this indefinitely.
'''
def main():
    # Per Logan, adding "+<number>" will make an email address unique but send it to the same place
    email_address_unique_number = 1

    # An enterprise solution would make these configurable.  I don't give a fuck so I'm hardcoding them.
    root_email_address = 'your_email_here@fake.com'
    first_name = 'Jamie'
    last_name = 'Lannister'
    phone_number = '314-123-4567'
    zip = '63303'

    # Repeat forever.
    while (1):
        # Appending the +1 to the end before the '@'.  This turns "your_email_here" into "your_email_here+1"
        final_email = root_email_address.split('@')[0] + \
                      '+' + \
                      str(email_address_unique_number) + \
                      root_email_address.split('@')[1]

        # Calling this on each iteration of the loop to handle the stuff that happens every time
        submit(final_email, first_name, last_name, phone_number, zip)

        # Increment by 1 so we get a unique email each time
        email_address_unique_number += 1
        
        # Wait 31 seconds before going again
        time.sleep(31)

# Python needs you to call the function to actually do anything.  So we're doing that.
if __name__ == '__main__':
    main()