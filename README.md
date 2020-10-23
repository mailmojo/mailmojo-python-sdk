# MailMojo SDK for Python
v1 of the MailMojo API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 0.6.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

For more information, please visit [https://mailmojo.dev](https://mailmojo.dev)

## Requirements

Python 2.7 and 3.4+

## Installation & Usage
### pip install

We recommend you install with pip:

```sh
pip install mailmojo-sdk
```

Then import the package:
```python
import mailmojo_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools) is also possible.

Clone the repo and perform the installation:

```sh
git clone https://github.com/eliksir/mailmojo-python-sdk.git
cd mailmojo-python-sdk
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mailmojo_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mailmojo_sdk
from mailmojo_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
configuration = mailmojo_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo_sdk.AccountApi(mailmojo_sdk.ApiClient(configuration))
user = mailmojo_sdk.UserCreation() # UserCreation | 

try:
    # Create an account.
    api_response = api_instance.create_account(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mailmojo.no*

Class | Method | HTTP request | Description
--- | --- | --- | ---
*AccountApi* | [create_account](docs/AccountApi.md#create_account) | **POST** /v1/accounts/ | Create an account.
*AccountApi* | [get_account_by_username](docs/AccountApi.md#get_account_by_username) | **GET** /v1/accounts/{username}/ | Retrieve account details.
*AccountApi* | [get_domain](docs/AccountApi.md#get_domain) | **GET** /v1/domains/{domain}/ | Retrieve domain details and authentication status.
*AccountApi* | [update_account](docs/AccountApi.md#update_account) | **POST** /v1/accounts/{username}/ | Update account details.
*AutomationApi* | [get_campaign_by_id](docs/AutomationApi.md#get_campaign_by_id) | **GET** /v1/campaigns/{campaign_id}/ | Retrieve an automation campaign by id.
*ContactApi* | [get_contact_by_email](docs/ContactApi.md#get_contact_by_email) | **GET** /v1/contacts/{email}/ | Retrieve a contact in any list by email.
*ContactApi* | [get_contacts](docs/ContactApi.md#get_contacts) | **GET** /v1/contacts/ | Retrieve all contacts across every list.
*ContactApi* | [get_historical_contact_stats](docs/ContactApi.md#get_historical_contact_stats) | **GET** /v1/contacts/stats/ | Retrieve historical stats over contacts across every list.
*ContactApi* | [get_subscriber_on_list_by_email](docs/ContactApi.md#get_subscriber_on_list_by_email) | **GET** /v1/lists/{list_id}/subscribers/{email}/ | Retrieve a subscriber.
*ContactApi* | [get_subscribers_on_list](docs/ContactApi.md#get_subscribers_on_list) | **GET** /v1/lists/{list_id}/subscribers/ | Retrieve subscribers on a list.
*ContactApi* | [get_unsubscribed_on_list](docs/ContactApi.md#get_unsubscribed_on_list) | **GET** /v1/lists/{list_id}/unsubscribed/ | Retrieve unsubscribed contacts on a list.
*ContactApi* | [subscribe_contact_to_list](docs/ContactApi.md#subscribe_contact_to_list) | **POST** /v1/lists/{list_id}/subscribers/ | Subscribe a contact to the email list.
*ContactApi* | [unsubscribe_contact_on_list_by_email](docs/ContactApi.md#unsubscribe_contact_on_list_by_email) | **DELETE** /v1/lists/{list_id}/subscribers/{email}/ | Unsubscribe a contact.
*ContactApi* | [update_contact](docs/ContactApi.md#update_contact) | **PATCH** /v1/contacts/{email}/ | Update details about a contact.
*EmbedApi* | [create_embed_session](docs/EmbedApi.md#create_embed_session) | **POST** /v1/embed/ | Create a new embedded application session.
*FormApi* | [form_add_subscriber](docs/FormApi.md#form_add_subscriber) | **PATCH** /v1/forms/{id}/subscribers/ | Add a subscriber through a form and track the conversion.
*FormApi* | [get_form_by_id](docs/FormApi.md#get_form_by_id) | **GET** /v1/forms/{id}/ | Retrieve a form.
*FormApi* | [get_forms](docs/FormApi.md#get_forms) | **GET** /v1/forms/ | Retrieve all forms.
*FormApi* | [track_form_view](docs/FormApi.md#track_form_view) | **PATCH** /v1/forms/{id}/track/view/ | Track a view of a form.
*FormApi* | [update_form](docs/FormApi.md#update_form) | **PATCH** /v1/forms/{id}/ | Update a form partially.
*ListApi* | [create_segment](docs/ListApi.md#create_segment) | **POST** /v1/lists/{list_id}/segments/ | Create a segment in the email list.
*ListApi* | [get_list_by_id](docs/ListApi.md#get_list_by_id) | **GET** /v1/lists/{list_id}/ | Retrieve an email list.
*ListApi* | [get_lists](docs/ListApi.md#get_lists) | **GET** /v1/lists/ | Retrieve all email lists.
*ListApi* | [get_subscriber_on_list_by_email](docs/ListApi.md#get_subscriber_on_list_by_email) | **GET** /v1/lists/{list_id}/subscribers/{email}/ | Retrieve a subscriber.
*ListApi* | [get_subscribers_on_list](docs/ListApi.md#get_subscribers_on_list) | **GET** /v1/lists/{list_id}/subscribers/ | Retrieve subscribers on a list.
*ListApi* | [get_unsubscribed_on_list](docs/ListApi.md#get_unsubscribed_on_list) | **GET** /v1/lists/{list_id}/unsubscribed/ | Retrieve unsubscribed contacts on a list.
*ListApi* | [import_subscribers_to_list](docs/ListApi.md#import_subscribers_to_list) | **POST** /v1/lists/{list_id}/subscribers/import/ | Subscribe contacts to the email list.
*ListApi* | [subscribe_contact_to_list](docs/ListApi.md#subscribe_contact_to_list) | **POST** /v1/lists/{list_id}/subscribers/ | Subscribe a contact to the email list.
*ListApi* | [unsubscribe_contact_on_list_by_email](docs/ListApi.md#unsubscribe_contact_on_list_by_email) | **DELETE** /v1/lists/{list_id}/subscribers/{email}/ | Unsubscribe a contact.
*ListApi* | [update_list](docs/ListApi.md#update_list) | **PATCH** /v1/lists/{list_id}/ | Update an email list partially.
*NewsletterApi* | [cancel_newsletter](docs/NewsletterApi.md#cancel_newsletter) | **PUT** /v1/newsletters/{newsletter_id}/cancel/ | Cancel a newsletter.
*NewsletterApi* | [create_newsletter](docs/NewsletterApi.md#create_newsletter) | **POST** /v1/newsletters/ | Create a newsletter draft.
*NewsletterApi* | [get_newsletter_by_id](docs/NewsletterApi.md#get_newsletter_by_id) | **GET** /v1/newsletters/{newsletter_id}/ | Retrieve a newsletter by id.
*NewsletterApi* | [get_newsletters](docs/NewsletterApi.md#get_newsletters) | **GET** /v1/newsletters/ | Retrieve all newsletters.
*NewsletterApi* | [send_newsletter](docs/NewsletterApi.md#send_newsletter) | **PUT** /v1/newsletters/{newsletter_id}/send/ | Send a newsletter.
*NewsletterApi* | [test_newsletter](docs/NewsletterApi.md#test_newsletter) | **POST** /v1/newsletters/{newsletter_id}/send_test/ | Send a test newsletter.
*NewsletterApi* | [update_newsletter](docs/NewsletterApi.md#update_newsletter) | **PATCH** /v1/newsletters/{newsletter_id}/ | Update a newsletter draft partially.
*PageApi* | [get_page_by_id](docs/PageApi.md#get_page_by_id) | **GET** /v1/pages/{id}/ | Retrieve a landing page.
*PageApi* | [get_pages](docs/PageApi.md#get_pages) | **GET** /v1/pages/ | Retrieve all landing pages.
*PageApi* | [track_page_view](docs/PageApi.md#track_page_view) | **PATCH** /v1/pages/{id}/track/view/ | Track a view of a landing page.
*PageApi* | [update_page](docs/PageApi.md#update_page) | **PATCH** /v1/pages/{id}/ | Update a landing page partially.
*SegmentApi* | [create_segment](docs/SegmentApi.md#create_segment) | **POST** /v1/lists/{list_id}/segments/ | Create a segment in the email list.
*TemplateApi* | [get_templates](docs/TemplateApi.md#get_templates) | **GET** /v1/templates/ | Retrieve all templates.
*WebhookApi* | [create_webhook](docs/WebhookApi.md#create_webhook) | **POST** /v1/webhooks/ | Create a webhook.
*WebhookApi* | [delete_webhook](docs/WebhookApi.md#delete_webhook) | **DELETE** /v1/webhooks/{id}/ | Delete a webhook.


## Documentation For Models

 - [AddFormSubscriber](docs/AddFormSubscriber.md)
 - [BaseContact](docs/BaseContact.md)
 - [CampaignDetail](docs/CampaignDetail.md)
 - [CampaignStatistics](docs/CampaignStatistics.md)
 - [Category](docs/Category.md)
 - [Contact](docs/Contact.md)
 - [ContactList](docs/ContactList.md)
 - [Contacts](docs/Contacts.md)
 - [Domain](docs/Domain.md)
 - [Embed](docs/Embed.md)
 - [EmbedOptions](docs/EmbedOptions.md)
 - [Form](docs/Form.md)
 - [FormConversion](docs/FormConversion.md)
 - [HistoricalContactsStats](docs/HistoricalContactsStats.md)
 - [ImportResult](docs/ImportResult.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [List](docs/List.md)
 - [ListDetail](docs/ListDetail.md)
 - [MinimalSegment](docs/MinimalSegment.md)
 - [NewsletterCreation](docs/NewsletterCreation.md)
 - [NewsletterDetail](docs/NewsletterDetail.md)
 - [NewsletterSend](docs/NewsletterSend.md)
 - [NewsletterSendTest](docs/NewsletterSendTest.md)
 - [NewsletterUpdate](docs/NewsletterUpdate.md)
 - [Page](docs/Page.md)
 - [PageMeta](docs/PageMeta.md)
 - [Schema](docs/Schema.md)
 - [Segment](docs/Segment.md)
 - [SegmentCreation](docs/SegmentCreation.md)
 - [SegmentTagPredicate](docs/SegmentTagPredicate.md)
 - [Statistics](docs/Statistics.md)
 - [Subscriber](docs/Subscriber.md)
 - [Template](docs/Template.md)
 - [TrackFormView](docs/TrackFormView.md)
 - [TrackPageView](docs/TrackPageView.md)
 - [User](docs/User.md)
 - [UserCreation](docs/UserCreation.md)
 - [WebhookCreation](docs/WebhookCreation.md)


## Documentation For Authorization


## mailmojo_auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://api.mailmojo.no/oauth/authorize/
- **Scopes**: 
  - **account**: Manage your MailMojo account.
  - **account_creation**: Create new MailMojo accounts.
  - **account_creation.trial_30**: Create new MailMojo accounts with a 30 day trial period.
  - **account_settings**: Manage your MailMojo account settings.
  - **campaigns**: Manage your automated campaigns.
  - **campaigns:read**: Retrieve your automated campaigns.
  - **contacts**: Manage your contacts across all your email lists.
  - **contacts:read**: Retrieve your contacts across all your email lists.
  - **embed**: Give you an embedded MailMojo application with access to your account.
  - **events**: Track events on your forms and landing pages.
  - **forms**: Manage your forms.
  - **forms:read**: Retrieve your forms.
  - **lists**: Manage your email lists, excluding subscribers.
  - **lists:read**: Retrieve your email lists, excluding subscribers.
  - **newsletters**: Manage your newsletters.
  - **newsletters:read**: Retrieve your newsletters.
  - **pages**: Manage your landing pages.
  - **pages:read**: Retrieve your landing pages.
  - **subscribe**: Add subscribers to email lists.
  - **templates**: Manage your templates.
  - **templates:read**: Retrieve your templates
  - **webhooks**: Manage your webhooks.


## Author

hjelp@mailmojo.no

