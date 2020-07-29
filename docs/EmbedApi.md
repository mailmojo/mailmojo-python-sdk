# mailmojo_sdk.EmbedApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embed_session**](EmbedApi.md#create_embed_session) | **POST** /v1/embed/ | Create a new embedded application session.


# **create_embed_session**
> str create_embed_session(embed)

Create a new embedded application session.

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
api_instance = mailmojo_sdk.EmbedApi(mailmojo_sdk.ApiClient(configuration))
embed = mailmojo_sdk.Embed() # Embed | 

try:
    # Create a new embedded application session.
    api_response = api_instance.create_embed_session(embed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmbedApi->create_embed_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed** | [**Embed**](Embed.md)|  | 

### Return type

**str**

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

