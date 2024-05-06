#VIEW ELEMENTS
logo_page_xpath = "//img[@alt='Practice Test Automation']"
header_page_xpath = "//h1[text()='Practice Test Automation']"
home_header_option_xpath = "//a[@href='https://practicetestautomation.com/']"
home_header_practice_option_xpath = "//a[@href='https://practicetestautomation.com/practice/']"
home_header_courses_option_xpath = "//a[@href='https://practicetestautomation.com/courses/']"
home_header_blog_option_xpath = "///a[@href='https://practicetestautomation.com/blog/']"
home_header_contact_option_xpath = "//a[@href='https://practicetestautomation.com/contact/']"

#LOGIN ELEMENTS
title_page_xpath = "//h2[contains(text(), 'Test login')]"
username_input = "//input[contains(@name,'username')]"
username="student"
password_input = "//input[contains(@name,'password')]"
password="Password123"
login_button_xpath = "//button[@id='submit' and @class='btn']"
title_sucessful_login_xpath = "//h1[@class='post-title'][contains(.,'Logged In Successfully')]"
logout_button_xpath = "//a[contains(.,'Log out')]"