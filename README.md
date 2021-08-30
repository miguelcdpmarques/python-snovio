# Python-Snovio

Python library for interacting with the snov.io API

This is being developed to make it easier for Python users to interact with the API. It is just a light wrapper around the official API. 

All features should be supported with the exception of those that are related to lists. In any case, feel free to add features, I welcome pull requests. 


Powered by [Remote Crew](https://www.remotecrew.io/)

<img src="https://www.remotecrew.io/_nuxt/img/14a498b.png" alt="Remote Crew"  height="50px">

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

### Installation

Python-snovio has been developed in Python 3.x. Some adjustments might be necessary to run in Python 2.x

Install the package using the following command.

```sh
$ pip install python-snovio
```

### User Guide

##### Setup
Start by importing the class from the package. 

```
from snovio import SnovioAPI
```
The next step is to get the credentials from the [API](https://app.snov.io/api-setting) tab of your account at Snov.io.

```
SNOVIO_USER_ID = 'your-user-id'
SNOVIO_USER_SECRET = 'your-user-secret' 
```

Finally, initialize the instance of `SnovioAPI` with your credentials.

```
snovio = SnovioAPI(client_id=SNOVIO_USER_ID, client_secret=SNOVIO_USER_SECRET)
```

If you'd prefer to use your access_token instead, you can also initialize the instance using it directly. 

```
snovio = SnovioAPI(access_token=ACCESS_TOKEN)
```


### Requests

You can now start to make requests using your account. See below the requests you can make, along with their cost in Credits.

##### EMAIL FINDER

- **2 Credits**: Domain Search v.2 √
    ```
    snovio.domain_emails_with_info({
        'domain':'riskpulse.com',
        'type': 'all',
        'limit': 100,
        'lastId': 0
    })
    ```

- **Free**: Get domain emails count √
    ```
    snovio.get_domain_emails_count({
        'domain': 'riskpulse.com'
    }) 
    ```

- **1 Credit**: Get emails from names √
    ```
    snovio.get_emails_from_names({
       'firstName': 'Joe',
       'lastName': 'Thomas',
       'domain': 'loom.com'
    })
    ```

- **1 Credit**: Add names to find emails √
    ```
    snovio.add_names_to_find_emails({
       'firstName': 'Joe',
       'lastName': 'Thomas',
       'domain': 'loom.com'
    })
    ```

- **1 Credit**: Add URL to search for prospect √
    ```
    snovio.add_url_for_search({
       'url': 'https://www.linkedin.com/in/elie-ohayon-aaab7341'
    })
    ```

- **1 Credit**: Get prospect with URL √
    ```
    snovio.get_emails_from_url({
       'url': 'https://www.linkedin.com/in/elie-ohayon-aaab7341'
    })
    ```

- **1 Credit:** Get profile by email √
    ```
    snovio.get_profile_by_email({
       'email': 'lizi.hamer@octagon.com',
    })
    ```

##### EMAIL VERIFIER

- **FREE:** Get emails verification status √
    ```
    snovio.get_emails_verification_status({
        'emails': ['gavin.vanrooyen@octagon.com', 'lizi.hamer@octagon.com']
    })
    ```

- **0.5 Credits:** Add emails to verification: √
    ```
    snovio.add_emails_to_verification({
       'emails': ['sales@riskpulse.com', 'lizi.hamer@octagon.com']
    })
    ```

##### DRIP CAMPAIGNS

- **Free**: Change recipient’s status √
    ```
    snovio.change_recipient_status({
        'email': 'gavin.vanrooyen@octagon.com',
        'campaign_id': 1234567,
        'status': 'Active'
    })
    ```

- **Free**:  See list of completed prospects √
    ```
    snovio.prospect_finished({
        'campaignId': 1234567
    })
    ```

- **Free**:  See campaign replies √
    ```
    snovio.get_emails_replies({
        'campaignId': 1234567
    })
    ```

- **Free**: Check link clicks √
    ```
    snovio.get_emails_clicked({
        'campaignId': 1234567
    })
    ```

- **Free**: View sent emails √
    ```
    snovio.emails_sent({
        'campaignId': 1234567
    })
    ```

- **Free**: View all campaigns √
    ```
    snovio.get_user_campaigns()
    ```

- **Free**: Add to Do-not-email List √
    ```
    snovio.do_not_email_list({
        'items[]': ['gavin.vanrooyen@octagon.com', 'octagon.com']
    })
    ```

##### PROSPECT MANAGEMENT

- **Free**: Add prospect to list √
    ```
    snovio.add_prospect_to_list({
        'email': 'john.doe@example.com',
        'fullName': 'John Doe',
        'firstName': 'John',
        'lastName': 'Doe',
        'country': 'United States',
        'locality': 'Woodbridge, New Jersey',
        'socialLinks[linkedIn]': 'https://www.linkedin.com/in/johndoe/&social',
        'social[twitter]': 'https://twitter.com/johndoe&social',
        'customFields[phone number]': '+ 1 888 2073333',
        'position': 'Vice President of Sales',
        'companyName': 'GoldenRule',
        'companySite': 'https://goldenrule.com',
        'updateContact': 1,
        'listId': '7508737'
    })
    ```

- **Free**: Find prospect by ID √
    ```
    snovio.get_prospect_by_id({
        'id': '66773b4a7e7b84180d2d8ed71a6a1fc657c22b7d38cc5684053faeb15ec8f392b874f87423'
    })
    ```

- **Free**: Find prospect by Email √
    ```
    snovio.get_prospects_by_email({
        'email': 'john.doe@example.com'
    })
    ```

- **Free**: Find prospect’s custom fields √
    ```
    snovio.prospect_custom_fields()
    ```

- **Free**: See user lists √
    ```
    snovio.get_user_lists()
    ```

- **Free**: View prospects in list √
    ```
    snovio.prospect_list({
        'listId': '7508737',
        'page': 1,
        'perPage': 10
    })
    ```

- **Free**: Create new prospects list √
    ```
    snovio.lists({
        'name': 'Test Lists',
    })
    ```

##### USER ACCOUNT

- **Free**: Check user balance √
    ```
    snovio.get_balance()
    ```
