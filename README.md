# Email Automation Script

This Python script automates the process of sending personalized emails with attachments. It's designed to assist with campaigns like "Join the fight to keep Compost in NYC," targeting recipients whose information is stored in an XLSX file converted to CSV for processing. Before using the automation, it's crucial to ensure the data is clean and properly formatted to avoid errors and maximize the effectiveness of your communication.

## Data Preparation and Cleaning
Before running the script, the data extracted from your CSV file needs to be cleaned and prepared. This process ensures that the information used is accurate, relevant, and formatted correctly, which is essential for personalizing emails and avoiding errors during the sending process.

## Steps for Data Cleaning
1. Removing Unnecessary Rows and Columns: Begin by eliminating any data not directly relevant to your email campaign. This includes redundant rows and columns that do not contain information needed for sending emails.
2. Standardizing Data Formats: Ensure that all data, especially dates and numerical values, follow a consistent format. This uniformity is crucial for automating personalized content in emails.
3. Validating and Correcting Errors: Utilize regular expressions to validate email addresses and other critical information. Correct any errors found to ensure that all recipients are reachable and that the data is accurate.
4. Extracting Email Addresses: Since contact information may include a mixture of emails, phone numbers, and notes, use regular expressions to accurately extract email addresses from this data.
5. Handling Missing Data: Determine a strategy for dealing with incomplete data entries, such as skipping these records or filling in missing information with default values.

## Features

- Extracts recipient details from a CSV file.
- Supports HTML email body content for rich text formatting.
- Sends emails with multiple attachments.
- Uses regular expressions to extract email addresses from contact information.
- Logs success and error messages for email delivery.

## Prerequisites

- Python 3.x
- A Gmail account with "Less secure app access" enabled or an App Password if Two-Factor Authentication (2FA) is enabled.
- Your CSV file should be formatted with specific columns (more details in the "CSV File Format" section).

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the script to your local machine.
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
## Usage
1. Prepare your CSV file named PartnerForCompost.csv with the required format.
2. Edit the script to fill in the placeholders for from_email and password with your Gmail account details.
3. Place your attachments in the same directory as the script or specify their paths in the script.
4. Run the script:
```bash
python email_sender.py
```
## CVS File Format
CSV should have the following columns:
- Status: Whether the email has been sent or not.
- Amount: Amount of compost each recipient has obtained.
- Date: The date you last worked with them.
- Contact: The contact information, including email addresses.

The script expects the CSV file to skip the first two rows (usually reserved for headers and titles) and starts reading from the third row.

## Configuring the Email Content
The HTML template for email content is stored in HTML_Template. Modify it to fit your campaign's message, ensuring to keep the placeholders {amount} and {date} if personalizing emails based on recipient details.
