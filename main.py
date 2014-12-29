from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

chromedriver = '/Users/abhyudaya/Downloads/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.quora.com")

#Logging in
email = driver.find_elements_by_name('email')
email[1].send_keys('abhyu195@gmail.com') #your email
password = driver.find_elements_by_name('password')
password[1].send_keys('timeparadox') #your password
password[1].send_keys(Keys.RETURN)
#Login complete

time.sleep(10)

#navigate to answer
driver.get('http://www.quora.com/How-can-I-write-Python-script-to-automatically-edit-my-answers-on-Quora/answers/5081090')
print('page loaded')


#get number of votes
upvotes = driver.find_element_by_class_name('answer_voters')
newValue = upvotes.text.split(' ')[0]

#open edit
edit = driver.find_elements_by_css_selector('a.edit.inline_editor_edit.suggested_edits')
#make edit visible to click
#selenium doesn't allow clicking of non visible elements
driver.execute_script("arguments[0].style.visibility = 'visible';",edit[0])
edit[0].click()
#edit clicked and opened

time.sleep(10)

#find the text box(text editor of quora)
text = driver.find_elements_by_css_selector('div.qtext_editor_content.qed_content')
print(text)

#I believe there are 3 of these. 1 for the question 1 for the question details and
#last for my answer (since this is the page where only my existing answer shows
#on the all answers page i suppose there would be more
#clear the text and update with new number
text[2].clear()
text[2].send_keys(newValue)

#the update button class was used by many more buttons so i just had to hit and trial
#on all of them till the correct one was hit
#very unsafe
update = driver.find_elements_by_class_name('submit_button')
print(len(update))
for x in update:
    try:
        x.click()
    except :
        print("not the correct button")

