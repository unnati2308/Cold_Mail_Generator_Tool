# Cold_Mail_Generator_Tool
This Cold Mail Generator Tool is a Python-based application designed to help users generate personalized cold emails efficiently. This tool is particularly useful for professionals, marketers, and sales teams who need to send outreach emails to potential clients or partners. The tool allows users to input specific details about the recipient and the purpose of the email, and it generates a professionally written cold email template.

## Features:
- Personalized Email Generation: Creates customized cold emails based on user inputs.
- Dynamic Templates: Uses predefined templates that can be easily modified or extended.
- CSV Input Support: Allows bulk email generation by reading recipient details from a CSV file.
- Easy-to-Use CLI: Simple command-line interface for quick email generation.
- Customizable: Users can modify the email templates and add new ones as needed.

## How It Works:
### Job URL Analysis:
- The tool uses web scraping libraries (e.g., BeautifulSoup or requests) to extract job details from the provided URL.
- It identifies key information such as job title, company name, required skills, and job description.
### Email Generation:
- Based on the extracted details, the tool selects an appropriate email template from *chains.py*.
- It dynamically fills in the placeholders (e.g., job title, company name, skills) to create a personalized email.
### Output:
- The generated email is displayed on streamlit app by running the following code:
  ```
  streamlit run main.py
  ```

## Installation:
### Clone the repository to your local machine:
```
git clone https://github.com/unnati2308/Cold_Mail_Generator_Tool.git
```
### Navigate to the project directory:
```
cd Cold_Mail_Generator_Tool
```
### Install the required dependencies:
```
pip install -r requirements.txt
```
## Working of the model:





https://github.com/user-attachments/assets/9f9621f2-bd55-4e70-9270-7b22a9082210



