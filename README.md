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
add
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


##### Requests

You can now start to make requests using your account. Here are some of the most relevant requests you are likely to use, along with their cost in Credits.

- **FREE:** Get domain emails count: √
    ```
    snovio.get_domain_emails_count({
        'domain': 'riskpulse.com'
    })
    ```
- **2 Credits:**  Get domain emails with info: √
    ```
    snovio.get_domain_emails_with_info({
        'domain':'riskpulse.com',
        'type': 'all',
        'limit': 100,
        'offset': 0
    })
    ```
- **FREE:**  Get emails verification status √
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
- **1 Credit:** Get emails from names √
    ```
    snovio.get_emails_from_names({
       'firstName': 'Joe',
       'lastName': 'Thomas',
       'domain': 'loom.com'
    })
    ```
- **1 Credit:** Add names to find emails √
    ```
    snovio.add_names_to_find_emails({
       'firstName': 'Joe',
       'lastName': 'Thomas',
       'domain': 'loom.com'
    })
    ```
- **1 Credit:** Get profile by email √
    ```
    snovio.get_profile_by_email({
       'email': 'lizi.hamer@octagon.com',
    })
    ```
