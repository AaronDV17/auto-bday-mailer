# Automated Birthday Mailer
Tips:
- Add your own SMTP email credentials to a .env file located in the directory
- If you don't use gmail, you'll have to edit the send_emails function in main.py to have the correct details of your SMTP host (usually found through a quick google search)
- Update birthdays.csv to contain the details of people you would like to automatically send a birthday email to
- Edit or add your own letter templates as .txt files in the letter_templates directory
- Lastly, host the code at <a href="https://www.pythonanywhere.com">PythonAnywhere</a> (or another cloud provider of your choice) if you want to schedule it to run daily in the cloud
