# mailmojo.CampaignApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_by_id**](CampaignApi.md#get_campaign_by_id) | **GET** /campaigns/{campaign_id}/ | Retrieve an automation campaign by id.


# **get_campaign_by_id**
> CampaignDetail get_campaign_by_id(campaign_id)

Retrieve an automation campaign by id.

### Example
```python
from __future__ import print_function
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailmojo.CampaignApi()
campaign_id = 56 # int | ID of the automation campaign to retrieve.

try:
    # Retrieve an automation campaign by id.
    api_response = api_instance.get_campaign_by_id(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->get_campaign_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| ID of the automation campaign to retrieve. | 

### Return type

[**CampaignDetail**](CampaignDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

