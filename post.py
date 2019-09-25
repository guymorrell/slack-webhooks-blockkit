import slack
import json
import requests

with open("block.json", "rt") as block_f:
    data = json.load(block_f)

def post_to_slack(message):
    webhook_url = 'https://hooks.slack.com/services/MY/WEBHOOK/URL'
    slack_data = json.dumps({'blocks': message})
    response = requests.post(
        webhook_url, data=slack_data,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

post_to_slack(data)
