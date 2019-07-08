# mailmojo_sdk.NewsletterApi

All URIs are relative to *https://api.mailmojo.no/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_newsletter**](NewsletterApi.md#create_newsletter) | **POST** /newsletters/ | Create a newsletter draft.
[**get_newsletter_by_id**](NewsletterApi.md#get_newsletter_by_id) | **GET** /newsletters/{newsletter_id}/ | Retrieve a newsletter by id.
[**get_newsletters**](NewsletterApi.md#get_newsletters) | **GET** /newsletters/ | Retrieve all newsletters.
[**send_newsletter**](NewsletterApi.md#send_newsletter) | **PUT** /newsletters/{newsletter_id}/send/ | Send a newsletter.
[**test_newsletter**](NewsletterApi.md#test_newsletter) | **POST** /newsletters/{newsletter_id}/send_test/ | Send a test newsletter.


# **create_newsletter**
> Newsletter create_newsletter(config=config)

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
config = mailmojo_sdk.NewsletterCreation() # NewsletterCreation |  (optional)

try:
    # Create a newsletter draft.
    api_response = api_instance.create_newsletter(config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsletterApi->create_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**NewsletterCreation**](NewsletterCreation.md)|  | [optional] 

### Return type

[**Newsletter**](Newsletter.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_newsletter_by_id**
> Newsletter get_newsletter_by_id(newsletter_id)

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

[**Newsletter**](Newsletter.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_newsletters**
> PaginatedResult get_newsletters(page=page, per_page=per_page, type=type)

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
type = 'type_example' # str | The type of newsletters to retrieve. Supported options are \"draft\", \"scheduled\" and \"sent\". (optional)

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
 **type** | **str**| The type of newsletters to retrieve. Supported options are \&quot;draft\&quot;, \&quot;scheduled\&quot; and \&quot;sent\&quot;. | [optional] 

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_newsletter**
> Newsletter send_newsletter(newsletter_id, config=config)

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

[**Newsletter**](Newsletter.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_newsletter**
> test_newsletter(newsletter_id, config=config)

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
config = mailmojo_sdk.NewsletterSendTest() # NewsletterSendTest |  (optional)

try:
    # Send a test newsletter.
    api_instance.test_newsletter(newsletter_id, config=config)
except ApiException as e:
    print("Exception when calling NewsletterApi->test_newsletter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newsletter_id** | **int**| ID of the newsletter to retrieve. | 
 **config** | [**NewsletterSendTest**](NewsletterSendTest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

