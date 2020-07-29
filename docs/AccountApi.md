# mailmojo_sdk.AccountApi

All URIs are relative to *https://api.mailmojo.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountApi.md#create_account) | **POST** /v1/accounts/ | Create an account.
[**get_account_by_username**](AccountApi.md#get_account_by_username) | **GET** /v1/accounts/{username}/ | Retrieve account details.
[**get_domain**](AccountApi.md#get_domain) | **GET** /v1/domains/{domain}/ | Retrieve domain details and authentication status.
[**update_account**](AccountApi.md#update_account) | **POST** /v1/accounts/{username}/ | Update account details.


# **create_account**
> User create_account(user)

Create an account.

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
api_instance = mailmojo_sdk.AccountApi(mailmojo_sdk.ApiClient(configuration))
user = mailmojo_sdk.UserCreation() # UserCreation | 

try:
    # Create an account.
    api_response = api_instance.create_account(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserCreation**](UserCreation.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_username**
> User get_account_by_username(username)

Retrieve account details.

This endpoint can be used to get details about your own account, or a subuser associated with you as a partner. If the username of your current authenticated user is unknown, you may use the special username 'me' to retrieve details about the authenticated user account.

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
api_instance = mailmojo_sdk.AccountApi(mailmojo_sdk.ApiClient(configuration))
username = 'username_example' # str | Username of the account to get details for, or the special username `me` to get details about your authenticated user.

try:
    # Retrieve account details.
    api_response = api_instance.get_account_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the account to get details for, or the special username &#x60;me&#x60; to get details about your authenticated user. | 

### Return type

[**User**](User.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> Domain get_domain(domain)

Retrieve domain details and authentication status.

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
api_instance = mailmojo_sdk.AccountApi(mailmojo_sdk.ApiClient(configuration))
domain = 'domain_example' # str | 

try:
    # Retrieve domain details and authentication status.
    api_response = api_instance.get_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> User update_account(username)

Update account details.

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
api_instance = mailmojo_sdk.AccountApi(mailmojo_sdk.ApiClient(configuration))
username = 'username_example' # str | Username of the user to update.

try:
    # Update account details.
    api_response = api_instance.update_account(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the user to update. | 

### Return type

[**User**](User.md)

### Authorization

[mailmojo_auth](../README.md#mailmojo_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

