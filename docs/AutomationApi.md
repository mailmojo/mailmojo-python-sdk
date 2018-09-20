# mailmojo_sdk.AutomationApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_by_id**](AutomationApi.md#get_campaign_by_id) | **GET** /campaigns/{campaign_id}/ | Retrieve an automation campaign by id.


# **get_campaign_by_id**
> CampaignDetail get_campaign_by_id(campaign_id)

Retrieve an automation campaign by id.

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
api_instance = mailmojo_sdk.AutomationApi(mailmojo_sdk.ApiClient(configuration))
campaign_id = 56 # int | ID of the automation campaign to retrieve.

try:
    # Retrieve an automation campaign by id.
    api_response = api_instance.get_campaign_by_id(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationApi->get_campaign_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| ID of the automation campaign to retrieve. | 

### Return type

[**CampaignDetail**](CampaignDetail.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

