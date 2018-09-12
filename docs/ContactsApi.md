# mailmojo.ContactsApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /contacts/{email}/ | Update details about a contact.


# **update_contact**
> MinimalContact update_contact(email, contact=contact)

Update details about a contact.

### Example
```python
from __future__ import print_function
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
configuration = mailmojo.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ContactsApi(mailmojo.ApiClient(configuration))
email = 'email_example' # str | Email address of contact to update.
contact = mailmojo.MinimalContact() # MinimalContact |  (optional)

try:
    # Update details about a contact.
    api_response = api_instance.update_contact(email, contact=contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of contact to update. | 
 **contact** | [**MinimalContact**](MinimalContact.md)|  | [optional] 

### Return type

[**MinimalContact**](MinimalContact.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

