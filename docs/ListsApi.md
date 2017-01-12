# mailmojo.ListsApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_by_id**](ListsApi.md#get_list_by_id) | **GET** /lists/{list_id}/ | Retrieve an email list.
[**get_lists**](ListsApi.md#get_lists) | **GET** /lists/ | Retrieve all email lists.
[**update_list**](ListsApi.md#update_list) | **PATCH** /lists/{list_id}/ | Update an email list partially.


# **get_list_by_id**
> List get_list_by_id(list_id)

Retrieve an email list.

### Example 
```python
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ListsApi()
list_id = 56 # int | ID of the email list to retrieve.

try: 
    # Retrieve an email list.
    api_response = api_instance.get_list_by_id(list_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->get_list_by_id: %s\n" % e
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
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ListsApi()

try: 
    # Retrieve all email lists.
    api_response = api_instance.get_lists()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->get_lists: %s\n" % e
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

# **update_list**
> List update_list(list_id)

Update an email list partially.

### Example 
```python
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.ListsApi()
list_id = 56 # int | ID of the email list to retrieve.

try: 
    # Update an email list partially.
    api_response = api_instance.update_list(list_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->update_list: %s\n" % e
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

