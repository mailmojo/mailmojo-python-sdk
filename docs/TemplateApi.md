# mailmojo_sdk.TemplateApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_templates**](TemplateApi.md#get_templates) | **GET** /v1/templates/ | Retrieve all templates.


# **get_templates**
> list[Template] get_templates()

Retrieve all templates.

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
api_instance = mailmojo_sdk.TemplateApi(mailmojo_sdk.ApiClient(configuration))

try:
    # Retrieve all templates.
    api_response = api_instance.get_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->get_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Template]**](Template.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

