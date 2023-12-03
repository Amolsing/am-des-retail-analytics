import sys
sys.path.append(r'E:\BW-PROJECT\am-des-retail-analytics\src\utils')

from vaultUtil import VaultClient
from awsUtil import AWSConnector

VAULT_URL = "http://127.0.0.1:8200"
ROLE_ID = "34d6e5b1-b78d-50f8-61b3-1cee61336451"
SECRET_ID = "726952c7-26bc-adb4-b6c4-6ed639847695"
SECRET_PATH = "secret/data/aws"

vault_client = VaultClient(VAULT_URL, ROLE_ID, SECRET_ID, SECRET_PATH)
token = vault_client.authenticate_with_approle()

if token:
    secret_data = vault_client.get_secret(token)
    if secret_data:
        aws_access_key = secret_data['data']['accesskey']
        aws_secret_key = secret_data['data']['secretkey']
        print("Secret data:", secret_data)
    else:
        print("Failed to retrieve secret.")
else:
    print("Failed to authenticate with AppRole.")

region = 'us-east-1'  # Replace with your preferred AWS region
aws_connector = AWSConnector(aws_access_key, aws_secret_key, 'iam', region)

# Access the IAM client through the instance
iam_client = aws_connector.aws_client_conn

# Now you can use iam_client to perform IAM operations
response = iam_client.list_groups()

print("IAM groups:", response)