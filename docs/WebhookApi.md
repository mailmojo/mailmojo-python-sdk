# mailmojo_sdk.WebhookApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /v1/webhooks/ | Create a webhook.
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /v1/webhooks/{id}/ | Delete a webhook.


# **create_webhook**
> WebhookCreation create_webhook(webhook)

Create a webhook.

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
api_instance = mailmojo_sdk.WebhookApi(mailmojo_sdk.ApiClient(configuration))
webhook = mailmojo_sdk.WebhookCreation() # WebhookCreation | 

try:
    # Create a webhook.
    api_response = api_instance.create_webhook(webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**WebhookCreation**](WebhookCreation.md)|  | 

### Return type

[**WebhookCreation**](WebhookCreation.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(id)

Delete a webhook.

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
api_instance = mailmojo_sdk.WebhookApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the webhook.

try:
    # Delete a webhook.
    api_instance.delete_webhook(id)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the webhook. | 

### Return type

void (empty response body)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

