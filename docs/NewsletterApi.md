# mailmojo_sdk.NewsletterApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_newsletter**](NewsletterApi.md#cancel_newsletter) | **PUT** /v1/newsletters/{newsletter_id}/cancel/ | Cancel a newsletter.
[**create_newsletter**](NewsletterApi.md#create_newsletter) | **POST** /v1/newsletters/ | Create a newsletter draft.
[**get_newsletter_by_id**](NewsletterApi.md#get_newsletter_by_id) | **GET** /v1/newsletters/{newsletter_id}/ | Retrieve a newsletter by id.
[**get_newsletters**](NewsletterApi.md#get_newsletters) | **GET** /v1/newsletters/ | Retrieve all newsletters.
[**send_newsletter**](NewsletterApi.md#send_newsletter) | **PUT** /v1/newsletters/{newsletter_id}/send/ | Send a newsletter.
[**test_newsletter**](NewsletterApi.md#test_newsletter) | **POST** /v1/newsletters/{newsletter_id}/send_test/ | Send a test newsletter.
[**update_newsletter**](NewsletterApi.md#update_newsletter) | **PATCH** /v1/newsletters/{newsletter_id}/ | Update a newsletter draft partially.


# **cancel_newsletter**
> NewsletterDetail cancel_newsletter(newsletter_id)

Cancel a newsletter.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
newsletter_id = 56 # int | ID of the newsletter to retrieve.

try:
    # Cancel a newsletter.
    api_response = api_instance.cancel_newsletter(newsletter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->cancel_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newsletter_id** | **int**| ID of the newsletter to retrieve. | 

### Return type

[**NewsletterDetail**](NewsletterDetail.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_newsletter**
> NewsletterDetail create_newsletter(newsletter)

Create a newsletter draft.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
newsletter = mailmojo_sdk.NewsletterCreation() # NewsletterCreation | 

try:
    # Create a newsletter draft.
    api_response = api_instance.create_newsletter(newsletter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->create_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newsletter** | [**NewsletterCreation**](NewsletterCreation.md)|  | 

### Return type

[**NewsletterDetail**](NewsletterDetail.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_newsletter_by_id**
> NewsletterDetail get_newsletter_by_id(newsletter_id)

Retrieve a newsletter by id.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
newsletter_id = 56 # int | ID of the newsletter to retrieve.

try:
    # Retrieve a newsletter by id.
    api_response = api_instance.get_newsletter_by_id(newsletter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->get_newsletter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newsletter_id** | **int**| ID of the newsletter to retrieve. | 

### Return type

[**NewsletterDetail**](NewsletterDetail.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_newsletters**
> InlineResponse200 get_newsletters(page=page, per_page=per_page, type=type)

Retrieve all newsletters.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
page = 1 # int | The current page of items (1 indexed). (optional) (default to 1)
per_page = 25 # int | The number of items returned per page. (optional) (default to 25)
type = 'type_example' # str | The type of newsletters to retrieve. Supported options are `draft`, `scheduled` and `sent`. (optional)

try:
    # Retrieve all newsletters.
    api_response = api_instance.get_newsletters(page=page, per_page=per_page, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->get_newsletters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page of items (1 indexed). | [optional] [default to 1]
 **per_page** | **int**| The number of items returned per page. | [optional] [default to 25]
 **type** | **str**| The type of newsletters to retrieve. Supported options are &#x60;draft&#x60;, &#x60;scheduled&#x60; and &#x60;sent&#x60;. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_newsletter**
> NewsletterDetail send_newsletter(newsletter_id, config=config)

Send a newsletter.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
newsletter_id = 56 # int | ID of the newsletter to retrieve.
config = mailmojo_sdk.NewsletterSend() # NewsletterSend |  (optional)

try:
    # Send a newsletter.
    api_response = api_instance.send_newsletter(newsletter_id, config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->send_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newsletter_id** | **int**| ID of the newsletter to retrieve. | 
 **config** | [**NewsletterSend**](NewsletterSend.md)|  | [optional] 

### Return type

[**NewsletterDetail**](NewsletterDetail.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_newsletter**
> test_newsletter(newsletter_id, config)

Send a test newsletter.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
newsletter_id = 56 # int | ID of the newsletter to retrieve.
config = mailmojo_sdk.NewsletterSendTest() # NewsletterSendTest | 

try:
    # Send a test newsletter.
    api_instance.test_newsletter(newsletter_id, config)
except ApiException as e:
    print("Exception when calling NewsletterApi->test_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newsletter_id** | **int**| ID of the newsletter to retrieve. | 
 **config** | [**NewsletterSendTest**](NewsletterSendTest.md)|  | 

### Return type

void (empty response body)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_newsletter**
> NewsletterDetail update_newsletter(id, newsletter=newsletter)

Update a newsletter draft partially.

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
api_instance = mailmojo_sdk.NewsletterApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the newsletter to update.
newsletter = mailmojo_sdk.NewsletterUpdate() # NewsletterUpdate |  (optional)

try:
    # Update a newsletter draft partially.
    api_response = api_instance.update_newsletter(id, newsletter=newsletter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->update_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the newsletter to update. | 
 **newsletter** | [**NewsletterUpdate**](NewsletterUpdate.md)|  | [optional] 

### Return type

[**NewsletterDetail**](NewsletterDetail.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

