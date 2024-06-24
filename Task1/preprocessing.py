import requests
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from minio import Minio
from io import BytesIO

url = "https://api.apilayer.com/tax_data/us_rate_list?state=NY"

payload = {}
headers = {"apikey": "UYpBgbs9eoWYJne1c509FnyyRznkrxu3"}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    # Correctly assign the parsed JSON data to 'tax_data'
    tax_data = response.json()
    # Extract the list of tax data from the 'data' key
    tax_data_list = tax_data.get('data', [])
    df = pd.DataFrame(tax_data_list)
else:
    print(f"Error fetching data. Status code: {response.status_code}")

df.ffill()
df.drop_duplicates(inplace=True)

# Step 4: Save the processed data in MinIO
# Initialize MinIO client
minio_client = Minio('play.min.io',
                     access_key='minioadmin',
                     secret_key='minioadmin',
                     secure=True)

# Convert DataFrame to Parquet
buffer = BytesIO()
table = pa.Table.from_pandas(df)
pq.write_table(table, buffer)
buffer.seek(0)

# Save Parquet file to MinIO
bucket_name = 'uni-bucket'
object_name = 'processed_data.parquet'

# Check if the bucket exists
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

# Upload the file
minio_client.put_object(bucket_name,
                        object_name,
                        data=buffer,
                        length=len(buffer.getvalue()),
                        content_type='application/octet-stream')

print(f"File successfully uploaded to MinIO at {bucket_name}/{object_name}")
