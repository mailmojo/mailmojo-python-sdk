# mailmojo_sdk.SegmentApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentApi.md#create_segment) | **POST** /v1/lists/{list_id}/segments/ | Create a segment in the email list.


# **create_segment**
> Segment create_segment(list_id, segment)

Create a segment in the email list.

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
api_instance = mailmojo_sdk.SegmentApi(mailmojo_sdk.ApiClient(configuration))
list_id = NULL # object | ID of the email list to create a segment in.
segment = mailmojo_sdk.SegmentCreation() # SegmentCreation | 

try:
    # Create a segment in the email list.
    api_response = api_instance.create_segment(list_id, segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | [**object**](.md)| ID of the email list to create a segment in. | 
 **segment** | [**SegmentCreation**](SegmentCreation.md)|  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

