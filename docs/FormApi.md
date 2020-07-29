# mailmojo_sdk.FormApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**form_add_subscriber**](FormApi.md#form_add_subscriber) | **PATCH** /v1/forms/{id}/subscribers/ | Add a subscriber through a form and track the conversion.
[**get_form_by_id**](FormApi.md#get_form_by_id) | **GET** /v1/forms/{id}/ | Retrieve a form.
[**get_forms**](FormApi.md#get_forms) | **GET** /v1/forms/ | Retrieve all forms.
[**track_form_view**](FormApi.md#track_form_view) | **PATCH** /v1/forms/{id}/track/view/ | Track a view of a form.
[**update_form**](FormApi.md#update_form) | **PATCH** /v1/forms/{id}/ | Update a form partially.


# **form_add_subscriber**
> FormConversion form_add_subscriber(id, subscriber)

Add a subscriber through a form and track the conversion.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the form.
subscriber = mailmojo_sdk.AddFormSubscriber() # AddFormSubscriber | 

try:
    # Add a subscriber through a form and track the conversion.
    api_response = api_instance.form_add_subscriber(id, subscriber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->form_add_subscriber: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the form. | 
 **subscriber** | [**AddFormSubscriber**](AddFormSubscriber.md)|  | 

### Return type

[**FormConversion**](FormConversion.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_by_id**
> Form get_form_by_id(id)

Retrieve a form.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the form to retrieve.

try:
    # Retrieve a form.
    api_response = api_instance.get_form_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->get_form_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the form to retrieve. | 

### Return type

[**Form**](Form.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms**
> list[Form] get_forms(is_published=is_published)

Retrieve all forms.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
is_published = false # bool | List only published forms. (optional) (default to false)

try:
    # Retrieve all forms.
    api_response = api_instance.get_forms(is_published=is_published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->get_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_published** | **bool**| List only published forms. | [optional] [default to false]

### Return type

[**list[Form]**](Form.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_form_view**
> TrackFormView track_form_view(id, view)

Track a view of a form.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the form to track view of.
view = mailmojo_sdk.TrackFormView() # TrackFormView | 

try:
    # Track a view of a form.
    api_response = api_instance.track_form_view(id, view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->track_form_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the form to track view of. | 
 **view** | [**TrackFormView**](TrackFormView.md)|  | 

### Return type

[**TrackFormView**](TrackFormView.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form**
> Form update_form(id, form=form)

Update a form partially.

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
api_instance = mailmojo_sdk.FormApi(mailmojo_sdk.ApiClient(configuration))
id = 56 # int | ID of the form to update.
form = mailmojo_sdk.Form() # Form |  (optional)

try:
    # Update a form partially.
    api_response = api_instance.update_form(id, form=form)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->update_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the form to update. | 
 **form** | [**Form**](Form.md)|  | [optional] 

### Return type

[**Form**](Form.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

