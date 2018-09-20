# mailmojo_sdk.ListApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_by_id**](ListApi.md#get_list_by_id) | **GET** /lists/{list_id}/ | Retrieve an email list.
[**get_lists**](ListApi.md#get_lists) | **GET** /lists/ | Retrieve all email lists.
[**get_subscriber_on_list_by_email**](ListApi.md#get_subscriber_on_list_by_email) | **GET** /lists/{list_id}/subscribers/{email}/ | Retrieve a subscriber.
[**get_subscribers_on_list**](ListApi.md#get_subscribers_on_list) | **GET** /lists/{list_id}/subscribers/ | Retrieve subscribers on a list.
[**import_subscribers_to_list**](ListApi.md#import_subscribers_to_list) | **POST** /lists/{list_id}/subscribers/import/ | Subscribe contacts to the email list.
[**subscribe_contact_to_list**](ListApi.md#subscribe_contact_to_list) | **POST** /lists/{list_id}/subscribers/ | Subscribe a contact to the email list.
[**unsubscribe_contact_on_list_by_email**](ListApi.md#unsubscribe_contact_on_list_by_email) | **DELETE** /lists/{list_id}/subscribers/{email}/ | Unsubscribe a contact.
[**update_list**](ListApi.md#update_list) | **PATCH** /lists/{list_id}/ | Update an email list partially.


# **get_list_by_id**
> List get_list_by_id(list_id)

Retrieve an email list.

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to retrieve.

try:
    # Retrieve an email list.
    api_response = api_instance.get_list_by_id(list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->get_list_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to retrieve. | 

### Return type

[**List**](List.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> list[List] get_lists()

Retrieve all email lists.

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))

try:
    # Retrieve all email lists.
    api_response = api_instance.get_lists()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->get_lists: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[List]**](List.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_on_list_by_email**
> list[Subscriber] get_subscriber_on_list_by_email(list_id, email)

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to retrieve the subscriber from. 
email = 'email_example' # str | Email address of the contact to retrieve.

try:
    # Retrieve a subscriber.
    api_response = api_instance.get_subscriber_on_list_by_email(list_id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->get_subscriber_on_list_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to retrieve the subscriber from.  | 
 **email** | **str**| Email address of the contact to retrieve. | 

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscribers_on_list**
> list[Subscriber] get_subscribers_on_list(list_id)

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list.

try:
    # Retrieve subscribers on a list.
    api_response = api_instance.get_subscribers_on_list(list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->get_subscribers_on_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list. | 

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_subscribers_to_list**
> ImportResult import_subscribers_to_list(list_id, contacts=contacts)

Subscribe contacts to the email list.

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to subscribe to.
contacts = [mailmojo_sdk.Contacts()] # list[Contacts] |  (optional)

try:
    # Subscribe contacts to the email list.
    api_response = api_instance.import_subscribers_to_list(list_id, contacts=contacts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->import_subscribers_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to subscribe to. | 
 **contacts** | [**list[Contacts]**](Contacts.md)|  | [optional] 

### Return type

[**ImportResult**](ImportResult.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_contact_to_list**
> Contact subscribe_contact_to_list(list_id, contact=contact)

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to subscribe to.
contact = mailmojo_sdk.Subscriber() # Subscriber |  (optional)

try:
    # Subscribe a contact to the email list.
    api_response = api_instance.subscribe_contact_to_list(list_id, contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->subscribe_contact_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to subscribe to. | 
 **contact** | [**Subscriber**](Subscriber.md)|  | [optional] 

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to unsubscribe from.
email = 'email_example' # str | Email address of the contact to unsubscribe.

try:
    # Unsubscribe a contact.
    api_response = api_instance.unsubscribe_contact_on_list_by_email(list_id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->unsubscribe_contact_on_list_by_email: %s\n" % e)
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

# **update_list**
> List update_list(list_id)

Update an email list partially.

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
api_instance = mailmojo_sdk.ListApi(mailmojo_sdk.ApiClient(configuration))
list_id = 56 # int | ID of the email list to retrieve.

try:
    # Update an email list partially.
    api_response = api_instance.update_list(list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to retrieve. | 

### Return type

[**List**](List.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

