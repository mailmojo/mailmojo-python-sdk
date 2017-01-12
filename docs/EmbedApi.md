# mailmojo.EmbedApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embed_session**](EmbedApi.md#create_embed_session) | **POST** /embed/ | Create a new embedded application session.


# **create_embed_session**
> str create_embed_session(config=config)

Create a new embedded application session.

### Example 
```python
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = mailmojo.EmbedApi()
config = mailmojo.Embed() # Embed |  (optional)

try: 
    # Create a new embedded application session.
    api_response = api_instance.create_embed_session(config=config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmbedApi->create_embed_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**Embed**](Embed.md)|  | [optional] 

### Return type

**str**

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

