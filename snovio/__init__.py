import requests
import json

SNOVIO_API_URL = 'https://api.snov.io/'
SNOVIO_USER_ID = 'your-user-id'
SNOVIO_USER_SECRET = 'your-user-secret'


class SnovioError(Exception):

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response


class IncorrectLoginError(SnovioError):
    pass


class SnovioAPI:
    GET_endpoints = [
        'domain-emails-with-info',
        'prospect-finished', 'get-emails-replies', 'get-emails-clicked',
        'get-user-campaigns', 'emails-sent',
        'get-prospect-by-id', 'get_prospects_by_email',
        'prospect-custom-fields', 'get-user-lists',
        'get-balance'
    ]

    def __init__(self, client_id=None, client_secret=None, access_token=None):
        if (not client_id and not client_secret) and not access_token:
            raise IncorrectLoginError('Please provide an access_token or client_id \
                and client_secret keys.')
        if not access_token:
            access_token = self.get_access_token(client_id, client_secret)

        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self, client_id, client_secret):
        auth_endpoint = 'oauth/access_token'
        params = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        response = requests.post(
            SNOVIO_API_URL + 'v1/' + auth_endpoint, data=params
        )
        resText = response.text.encode('ascii', 'ignore')
        return json.loads(resText)['access_token']

    def _request(self, endpoint, data):
        if self.is_parameter_in_uri(endpoint):
            endpoint = self.update_endpoint_with_query_params(endpoint, data)
            data = {}

        # Add authentication
        data['access_token'] = self.access_token

        if self.get_http_method(endpoint) == 'GET':
            response = requests.get(
                SNOVIO_API_URL + self.get_endpoint_version(endpoint) + endpoint,
                data=data
            )
        else:
            response = requests.post(
                SNOVIO_API_URL + self.get_endpoint_version(endpoint) + endpoint,
                data=data
            )
        # Response Validation
        if response.status_code == 200:
            response = response.json()
            response.pop('access_token', None)
            return response

        elif response.status_code == 401:
            print('Refreshing token')
            if self.is_parameter_in_uri(endpoint):
                endpoint = self.update_endpoint_with_query_params(endpoint, data)
                data = {}
            self.access_token = self.get_access_token(
                self.client_id, self.client_secret
            )
            data['access_token'] = self.access_token
            if self.get_http_method(endpoint) == 'GET':
                response = requests.get(
                    SNOVIO_API_URL + self.get_endpoint_version(endpoint) + endpoint,
                    params=data
                )
            else:
                response = requests.post(
                    SNOVIO_API_URL + self.get_endpoint_version(endpoint) + endpoint,
                    data=data
                )
            return response.json()

    def __getattr__(self, name):
        def wrapper(data={}):
            response = self._request(name.replace('_', '-'), data)
            if 'error' in response:
                raise SnovioError(response)
            return response
        return wrapper

    def get_http_method(self, endpoint):
        if endpoint in self.GET_endpoints:
            return 'GET'
        return 'POST'

    @staticmethod
    def get_endpoint_version(endpoint):
        version_2_endpoints = ['domain-emails-with-info']
        if endpoint in version_2_endpoints:
            return 'v2/'
        return 'v1/'

    @staticmethod
    def is_parameter_in_uri(endpoint):
        query_params_endpoints = [
            'get-emails-verification-status',
            'add-emails-to-verification',
        ]
        if endpoint in query_params_endpoints:
            return True
        return False

    @staticmethod
    def update_endpoint_with_query_params(endpoint, data):
        if not data.get('emails', False):
            raise SnovioError(
                f"'emails' parameter missing from request to endpoint {endpoint}."
            )

        updated_endpoint = endpoint + '?'
        for email in data['emails']:
            updated_endpoint = updated_endpoint + 'emails[]=' + email + '&'

        return updated_endpoint[:-1]  # remove the last &



if __name__ == "__main__":
    # Initialize the instance with your credentials
    snovio = SnovioAPI(client_id=SNOVIO_USER_ID, client_secret=SNOVIO_USER_SECRET)

    ###  EMAIL FINDER ###
    # 2 Credits: Domain Search v.2 √
    # domain_emails_with_info = snovio.domain_emails_with_info({
    #     'domain':'riskpulse.com',
    #     'type': 'all',
    #     'limit': 100,
    #     'lastId': 0
    # })
    # print(domain_emails_with_info)

    # FREE: Get domain emails count √
    # domain_emails_count = snovio.get_domain_emails_count({
    #     'domain': 'riskpulse.com'
    # }) 
    # print(domain_emails_count)

    # 1 Credit: Get emails from names √
    # emails_from_names = snovio.get_emails_from_names({
    #    'firstName': 'Joe',
    #    'lastName': 'Thomas',
    #    'domain': 'loom.com'
    # })
    # print(emails_from_names)

    # 1 Credit: Add names to find emails √
    # names_to_find_emails = snovio.add_names_to_find_emails({
    #    'firstName': 'Joe',
    #    'lastName': 'Thomas',
    #    'domain': 'loom.com'
    # })
    # print(names_to_find_emails)

    # 1 Credit: Add URL to search for prospect √
    # url_for_search = snovio.add_url_for_search({
    #    'url': 'https://www.linkedin.com/in/elie-ohayon-aaab7341'
    # })
    # print(url_for_search)

    # 1 Credit: Get prospect with URL √
    # emails_from_url = snovio.get_emails_from_url({
    #    'url': 'https://www.linkedin.com/in/elie-ohayon-aaab7341'
    # })
    # print(emails_from_url)

    # 1 Credit: Get profile by email √
    # profile_by_email = snovio.get_profile_by_email({
    #    'email': 'lizi.hamer@octagon.com',
    # })
    # print(profile_by_email)


    ###  EMAIL VERIFIER ###
    # FREE: Get emails verification status √
    # emails_verification_status = snovio.get_emails_verification_status({
    #     'emails': ['gavin.vanrooyen@octagon.com', 'lizi.hamer@octagon.com']
    # })
    # print(emails_verification_status)

    # 0.5 Credits: Add emails to verification √
    # emails_to_verification = snovio.add_emails_to_verification({
    #    'emails': ['sales@riskpulse.com', 'lizi.hamer@octagon.com']
    # })
    # print(emails_to_verification)

    ###  DRIP CAMPAIGNS ###

    # FREE: Change recipient’s status √
    # recipient_status = snovio.change_recipient_status({
    #     'email': 'gavin.vanrooyen@octagon.com',
    #     'campaign_id': 1234567,
    #     'status': 'Active'
    # })
    # print(recipient_status)

    # FREE: See list of completed prospects √
    # prospects = snovio.prospect_finished({
    #     'campaignId': 1234567
    # })
    # print(prospects)

    # FREE: See campaign replies √
    # email_replies = snovio.get_emails_replies({
    #     'campaignId': 1234567
    # })
    # print(email_replies)

    # FREE: Check link clicks √
    # emails_clicked = snovio.get_emails_clicked({
    #     'campaignId': 1234567
    # })
    # print(emails_clicked)

    # FREE: View sent emails √
    # emails_sent = snovio.emails_sent({
    #     'campaignId': 1234567
    # })
    # print(emails_sent)

    # FREE: View all campaigns √
    # user_campaigns = snovio.get_user_campaigns()
    # print(user_campaigns)

    # FREE: Add to Do-not-email List √
    # do_not_email_list = snovio.do_not_email_list({
    #     'items[]': ['gavin.vanrooyen@octagon.com', 'octagon.com']
    # })
    # print(do_not_email_list)

    ###  PROSPECT MANAGEMENT ###

    # FREE: Add prospect to list √
    # add_prospect_to_list = snovio.add_prospect_to_list({
    #     'email': 'john.doe@example.com',
    #     'fullName': 'John Doe',
    #     'firstName': 'John',
    #     'lastName': 'Doe',
    #     'country': 'United States',
    #     'locality': 'Woodbridge, New Jersey',
    #     'socialLinks[linkedIn]': 'https://www.linkedin.com/in/johndoe/&social',
    #     'social[twitter]': 'https://twitter.com/johndoe&social',
    #     'customFields[phone number]': '+ 1 888 2073333',
    #     'position': 'Vice President of Sales',
    #     'companyName': 'GoldenRule',
    #     'companySite': 'https://goldenrule.com',
    #     'updateContact': 1,
    #     'listId': '7508737'
    # })
    # print(add_prospect_to_list)

    # FREE: Find prospect by ID √
    # get_prospect_by_id = snovio.get_prospect_by_id({
    #     'id': '66773b4a7e7b84180d2d8ed71a6a1fc657c22b7d38cc5684053faeb15ec8f392b874f87423'
    # })
    # print(get_prospect_by_id)

    # FREE: Find prospect by Email √
    # get_prospects_by_email = snovio.get_prospects_by_email({
    #     'email': 'john.doe@example.com'
    # })
    # print(get_prospects_by_email)

    # FREE: Find prospect’s custom fields √
    # prospect_custom_fields = snovio.prospect_custom_fields()
    # print(prospect_custom_fields)

    # FREE: See user lists √
    # user_lists = snovio.get_user_lists()
    # print(user_lists)

    # FREE: View prospects in list √
    # prospect_list = snovio.prospect_list({
    #     'listId': '7508737',
    #     'page': 1,
    #     'perPage': 10
    # })
    # print(prospect_list)

    # FREE: Create new prospects list √
    # new_list = snovio.lists({
    #     'name': 'Test Lists',
    # })
    # print(new_list)

    ### USER ACCOUNT ###
    # FREE: Check user balance √
    # balance = snovio.get_balance()
    # print(balance)
