# mailmojo.ContactsApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /contacts/ | Retrieve all contacts across every list.
[**get_subscriber_on_list_by_email**](ContactsApi.md#get_subscriber_on_list_by_email) | **GET** /lists/{list_id}/subscribers/{email}/ | Retrieve a subscriber.
[**get_subscribers_on_list**](ContactsApi.md#get_subscribers_on_list) | **GET** /lists/{list_id}/subscribers/ | Retrieve subscribers on a list.
[**import_subscribers_to_list**](ContactsApi.md#import_subscribers_to_list) | **POST** /lists/{list_id}/subscribers/import/ | Subscribe contacts to the email list.
[**subscribe_contact_to_list**](ContactsApi.md#subscribe_contact_to_list) | **POST** /lists/{list_id}/subscribers/ | Subscribe a contact to the email list.
[**unsubscribe_contact_on_list_by_email**](ContactsApi.md#unsubscribe_contact_on_list_by_email) | **DELETE** /lists/{list_id}/subscribers/{email}/ | Unsubscribe a contact.


# **get_contacts**
> list[Contact] get_contacts()

Retrieve all contacts across every list.

This endpoint currently returns all contacts in your account *without any pagination* and should be considered EXPERIMENTAL. The response schema will change without any warning in the near future to account for pagination. 

### Example 
```python
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi()

try: 
    # Retrieve all contacts across every list.
    api_response = api_instance.get_contacts()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->get_contacts: %s\n" % e
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

# **get_subscriber_on_list_by_email**
> list[Subscriber] get_subscriber_on_list_by_email(list_id, email)

Retrieve a subscriber.

### Example 
```python
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi()
list_id = 56 # int | ID of the email list to retrieve the subscriber from. 
email = 'email_example' # str | Email address of the contact to retrieve.

try: 
    # Retrieve a subscriber.
    api_response = api_instance.get_subscriber_on_list_by_email(list_id, email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->get_subscriber_on_list_by_email: %s\n" % e
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
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi()
list_id = 56 # int | ID of the email list.

try: 
    # Retrieve subscribers on a list.
    api_response = api_instance.get_subscribers_on_list(list_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->get_subscribers_on_list: %s\n" % e
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
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi()
list_id = 56 # int | ID of the email list to subscribe to.
contacts = [mailmojo.Contacts()] # list[Contacts] |  (optional)

try: 
    # Subscribe contacts to the email list.
    api_response = api_instance.import_subscribers_to_list(list_id, contacts=contacts)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->import_subscribers_to_list: %s\n" % e
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
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi()
list_id = 56 # int | ID of the email list to subscribe to.
contact = mailmojo.Contact() # Contact |  (optional)

try: 
    # Subscribe a contact to the email list.
    api_response = api_instance.subscribe_contact_to_list(list_id, contact=contact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->subscribe_contact_to_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the email list to subscribe to. | 
 **contact** | [**Contact**](Contact.md)|  | [optional] 

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
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi()
list_id = 56 # int | ID of the email list to unsubscribe from.
email = 'email_example' # str | Email address of the contact to unsubscribe.

try: 
    # Unsubscribe a contact.
    api_response = api_instance.unsubscribe_contact_on_list_by_email(list_id, email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactsApi->unsubscribe_contact_on_list_by_email: %s\n" % e
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
