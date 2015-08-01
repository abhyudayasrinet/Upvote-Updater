from selenium import webdriver
import os
import time
import sys
from selenium.webdriver.common.keys import Keys

chromedriver = '/Users/abhyudaya/Downloads/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.quora.com")
print('quora loaded')

#Logging in
email = driver.find_elements_by_name('email')
email[1].send_keys('*********') #your email
password = driver.find_elements_by_name('password')
password[1].send_keys('********') #your password
password[1].send_keys(Keys.RETURN)
#Login complete

time.sleep(20)

#navigate to answer
driver.get('http://www.quora.com/How-can-I-write-Python-script-to-automatically-edit-my-answers-on-Quora/answers/5081090')
print('answer page loaded')

time.sleep(20)

#get number of votes
#the upvotes are stored in a span inside a div with class = "primary_item"
#the re-ask button has the same class so we get the elements with the class and
#take out the element with "Upvotes in its text"
upvoteCount = 0
primaryItemElements = driver.find_elements_by_class_name('primary_item')
for element in primaryItemElements:
    if(element.text.encode('ascii','ignore').find("Upvotes") >= 0):
        upvoteCount = int(element.text[7:].encode('ascii','ignore'))
        
print("new number of upvotes :"+str(upvoteCount))

#The edit answer button has been shifted to a pop up list which comes up
#when we click the dots at the bottom of the answer
#there are 2 such dots. one for the question and one for the answer
dots = driver.find_elements_by_class_name('overflow_link')
dots[1].click()

time.sleep(10)

#find the edit answer button and click it
#the edit answer button lies in an <a> tag inside a list with class "menu_list_item"
edit = driver.find_elements_by_class_name("menu_list_item")
for e in edit:
    try:
        inner_text = driver.execute_script("return arguments[0].innerText;", e)
        text = inner_text.encode('ascii','ignore').lower()
        print(text)
        print(text.find('edit answer'))
        if(text.find('edit answer') >= 0):
            e.click()
            print("edit answer clicked")
            break
    except :
        print("error in clicking")
        pass

time.sleep(20)

#find the text box(text editor of quora)
text = driver.find_elements_by_css_selector('div.qtext_editor_content.qed_content')
print(text)


answerText = "This answer has "+str(upvoteCount)+" upvotes.\n"
answerText += """The code is available here : https://github.com/abhyudayasrinet/Upvote-Updater
The script isn't running 24x7 so once you upvote the answer won't change i'll have to re run the script for it to change"""

#There are multiple textboxes but only the correct one will be available
#to edit but only one visible so loop through available ones and update the correct box
for textbox in text:
    try:
        textbox.clear()        
        textbox.send_keys(answerText)
    except :
        print("error in textbox")
        pass


time.sleep(10)

#the answer text box is in a div with class = "inline_editor_buttons"
#which has the update button so looping through all such elements and
#clicking the right one since only the correct one will be visible
editorDivs = driver.find_elements_by_class_name('inline_editor_buttons')
for editorDiv in editorDivs:
    try:
        updateButton = editorDiv.find_element_by_class_name('submit_button')
        updateButton.click()
        print("update clicked")
    except:
        print("error in update")
        pass
