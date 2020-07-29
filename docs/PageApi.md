# mailmojo_sdk.PageApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_page_by_id**](PageApi.md#get_page_by_id) | **GET** /v1/pages/{id}/ | Retrieve a landing page.
[**get_pages**](PageApi.md#get_pages) | **GET** /v1/pages/ | Retrieve all landing pages.
[**update_page**](PageApi.md#update_page) | **PATCH** /v1/pages/{id}/ | Update a landing page partially.


# **get_page_by_id**
> Page get_page_by_id(id)

Retrieve a landing page.

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
api_instance = mailmojo_sdk.PageApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the landing page to retrieve.

try:
    # Retrieve a landing page.
    api_response = api_instance.get_page_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageApi->get_page_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the landing page to retrieve. | 

### Return type

[**Page**](Page.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages**
> list[Page] get_pages()

Retrieve all landing pages.

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
api_instance = mailmojo_sdk.PageApi(mailmojo_sdk.ApiClient(configuration))

try:
    # Retrieve all landing pages.
    api_response = api_instance.get_pages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageApi->get_pages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Page]**](Page.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_page**
> Page update_page(id, page=page)

Update a landing page partially.

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
api_instance = mailmojo_sdk.PageApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the landing page to update.
page = mailmojo_sdk.Page() # Page |  (optional)

try:
    # Update a landing page partially.
    api_response = api_instance.update_page(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageApi->update_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the landing page to update. | 
 **page** | [**Page**](Page.md)|  | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

