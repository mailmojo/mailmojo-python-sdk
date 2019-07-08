# mailmojo_sdk.FormApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forms**](FormApi.md#get_forms) | **GET** /forms/ | Retrieve all forms.
[**update_form**](FormApi.md#update_form) | **PATCH** /forms/{id}/ | Update a form partially.


# **get_forms**
> list[Form] get_forms(is_published=is_published)

Retrieve all forms.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
is_published = false # bool | List only published forms. (optional) (default to false)

try:
    # Retrieve all forms.
    api_response = api_instance.get_forms(is_published=is_published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->get_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_published** | **bool**| List only published forms. | [optional] [default to false]

### Return type

[**list[Form]**](Form.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form**
> Form update_form(id)

Update a form partially.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the form to update.

try:
    # Update a form partially.
    api_response = api_instance.update_form(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->update_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the form to update. | 

### Return type

[**Form**](Form.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

