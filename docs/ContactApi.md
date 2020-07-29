# mailmojo_sdk.ContactApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contact_by_email**](ContactApi.md#get_contact_by_email) | **GET** /v1/contacts/{email}/ | Retrieve a contact in any list by email.
[**get_contacts**](ContactApi.md#get_contacts) | **GET** /v1/contacts/ | Retrieve all contacts across every list.
[**get_historical_contact_stats**](ContactApi.md#get_historical_contact_stats) | **GET** /v1/contacts/stats/ | Retrieve historical stats over contacts across every list.
[**get_subscriber_on_list_by_email**](ContactApi.md#get_subscriber_on_list_by_email) | **GET** /v1/lists/{list_id}/subscribers/{email}/ | Retrieve a subscriber.
[**get_subscribers_on_list**](ContactApi.md#get_subscribers_on_list) | **GET** /v1/lists/{list_id}/subscribers/ | Retrieve subscribers on a list.
[**get_unsubscribed_on_list**](ContactApi.md#get_unsubscribed_on_list) | **GET** /v1/lists/{list_id}/unsubscribed/ | Retrieve unsubscribed contacts on a list.
[**subscribe_contact_to_list**](ContactApi.md#subscribe_contact_to_list) | **POST** /v1/lists/{list_id}/subscribers/ | Subscribe a contact to the email list.
[**unsubscribe_contact_on_list_by_email**](ContactApi.md#unsubscribe_contact_on_list_by_email) | **DELETE** /v1/lists/{list_id}/subscribers/{email}/ | Unsubscribe a contact.
[**update_contact**](ContactApi.md#update_contact) | **PATCH** /v1/contacts/{email}/ | Update details about a contact.


# **get_contact_by_email**
> Contact get_contact_by_email(email)

Retrieve a contact in any list by email.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
email = 'email_example' # str | 

try:
    # Retrieve a contact in any list by email.
    api_response = api_instance.get_contact_by_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_contact_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> list[Contact] get_contacts()

Retrieve all contacts across every list.

This endpoint currently returns all contacts in your account *without any pagination* and should be considered EXPERIMENTAL. The response schema will change without any warning in the near future to account for pagination.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))

try:
    # Retrieve all contacts across every list.
    api_response = api_instance.get_contacts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_contacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Contact]**](Contact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_contact_stats**
> list[HistoricalContactsStats] get_historical_contact_stats(start_date=start_date)

Retrieve historical stats over contacts across every list.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
start_date = '2013-10-20' # date | The starting date to include stats from. (optional)

try:
    # Retrieve historical stats over contacts across every list.
    api_response = api_instance.get_historical_contact_stats(start_date=start_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_historical_contact_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| The starting date to include stats from. | [optional] 

### Return type

[**list[HistoricalContactsStats]**](HistoricalContactsStats.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_on_list_by_email**
> Subscriber get_subscriber_on_list_by_email(list_id, email)

Retrieve a subscriber.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to retrieve the subscriber from.
email = 'email_example' # str | Email address of the contact to retrieve.

try:
    # Retrieve a subscriber.
    api_response = api_instance.get_subscriber_on_list_by_email(list_id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_subscriber_on_list_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to retrieve the subscriber from. | 
 **email** | **str**| Email address of the contact to retrieve. | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscribers_on_list**
> list[Subscriber] get_subscribers_on_list(list_id, limit=limit)

Retrieve subscribers on a list.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list.
limit = 56 # int | Limits the result to given count. (optional)

try:
    # Retrieve subscribers on a list.
    api_response = api_instance.get_subscribers_on_list(list_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_subscribers_on_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list. | 
 **limit** | **int**| Limits the result to given count. | [optional] 

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribed_on_list**
> list[Contact] get_unsubscribed_on_list(list_id, limit=limit)

Retrieve unsubscribed contacts on a list.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list.
limit = 56 # int | Limits the result to given count. (optional)

try:
    # Retrieve unsubscribed contacts on a list.
    api_response = api_instance.get_unsubscribed_on_list(list_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_unsubscribed_on_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list. | 
 **limit** | **int**| Limits the result to given count. | [optional] 

### Return type

[**list[Contact]**](Contact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_contact_to_list**
> Contact subscribe_contact_to_list(list_id, contact)

Subscribe a contact to the email list.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to subscribe to.
contact = mailmojo_sdk.Subscriber() # Subscriber | 

try:
    # Subscribe a contact to the email list.
    api_response = api_instance.subscribe_contact_to_list(list_id, contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->subscribe_contact_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to subscribe to. | 
 **contact** | [**Subscriber**](Subscriber.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact_on_list_by_email**
> Contact unsubscribe_contact_on_list_by_email(list_id, email)

Unsubscribe a contact.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to unsubscribe from.
email = 'email_example' # str | Email address of the contact to unsubscribe.

try:
    # Unsubscribe a contact.
    api_response = api_instance.unsubscribe_contact_on_list_by_email(list_id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->unsubscribe_contact_on_list_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to unsubscribe from. | 
 **email** | **str**| Email address of the contact to unsubscribe. | 

### Return type

[**Contact**](Contact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> BaseContact update_contact(email, contact=contact)

Update details about a contact.

### Example
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
api_instance = mailmojo_sdk.ContactApi(mailmojo_sdk.ApiClient(configuration))
email = 'email_example' # str | Email address of contact to update.
contact = mailmojo_sdk.BaseContact() # BaseContact |  (optional)

try:
    # Update details about a contact.
    api_response = api_instance.update_contact(email, contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of contact to update. | 
 **contact** | [**BaseContact**](BaseContact.md)|  | [optional] 

### Return type

[**BaseContact**](BaseContact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

