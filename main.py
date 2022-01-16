import openreview
from openreview import Client
from tqdm import tqdm

import os
try:
    os.mkdir("zips")
except:
    pass

try:
    os.mkdir("vars")
except:
    pass

client = Client(baseurl='https://api.openreview.net', username="your email here", password="your pwd here")


ids = list(openreview.tools.iterget_notes(client, invitation = "invitation url here"))
for subs in tqdm(ids):
    id = subs.id
    zip = client.get_attachment(id, 'submission_full')
    url = client.get_attachment(id, 'blogpost_url')

    with open(f"zips/{id}.zip", 'wb') as f:
        f.write(zip)
    with open(f"vars/{id}.yml", 'wb') as f:
        f.write(url)

