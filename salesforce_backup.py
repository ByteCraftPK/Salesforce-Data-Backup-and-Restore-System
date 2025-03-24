from simple_salesforce import Salesforce
import pandas as pd

# Salesforce login details
USERNAME = "pranjalik189217@agentforce.com"
PASSWORD = "Pranjali@2004"
SECURITY_TOKEN = "zuCYxKYEPpEk9VJqGz380WCUo"
CONSUMER_KEY = "3MVG9dAEux2v1sLu2JmfjbUEVpFbt.wi1oEfsDyokwNY0.i1O3asJs0V7JUcxGvvGnLYCVY7Nf6__n_4Whldf"
CONSUMER_SECRET = "7B19E595205CDABB5721AB012A91DCA5B77826215006682C7E201AFB0E0329DB"

# Connect to Salesforce
sf = Salesforce(username=USERNAME, password=PASSWORD, security_token=SECURITY_TOKEN)

# Fetch Salesforce data (Example: Leads)
query = "SELECT Id, Name, Email FROM Lead"
data = sf.query_all(query)
records = data['records']

# Convert to DataFrame
df = pd.DataFrame(records)
df.drop(columns=['attributes'], inplace=True)  # Remove extra field

# Save as CSV
df.to_csv("salesforce_backup.csv", index=False)
print("Backup saved successfully!")
