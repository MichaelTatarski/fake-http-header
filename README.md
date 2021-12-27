# Fake http header

**fake-http-header** is a python package that you can use to generate random request fields for a http header. The generated header fields look like they might come from a real internet browser. It is accomplished by mapping browsers to default values and emulating real user behaviour. You can utilize this package, for instance, to write crawlers or for testing web applications.

## Installation

The easiest way to install this package is using pip. In case you have pip on your system, just type the following command into your terminal prompt:

```bash
pip install fake-http-header
```

## Quick Start

Generating a random http header is quite straight forward. Just import the package and call the construcor method for the FakeHttpHeader class without any parameters.

**Example:**
```python
from fake_http_header import FakeHttpHeader

fake_header = FakeHttpHeader()
print(fake_header)
```

__Output:__

```python
FakeHttpHeader(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43', accept_language='en-GB',  accept_encoding='identit,b',  accept='text/html, application/xhtml+xml, image/jxr, */*', referer='http://www.intute.ac.uk')
```
As you can see, the generated header contains an  **Accept-Language** field, which states that the client prefers british english __(accept_language='en-GB')__. To make this header look more plausible, the referrer site is thereby generated from a pool of **.uk** domains.

It is also possible to specify of which top level domain the **referer site** should be. In that case, a fitting **Accept-Language** field will be generated. 

**Example:**
```python
fake_header = FakeHttpHeader(browser_domain = 'de')
print(fake_header)
```
__Output:__

```python
FakeHttpHeader(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', accept_language='de', accept_encoding='deflat,b,compres', accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', referer='http://www.netluchs.de')
```
When working with other python libraries like __requests__, it is necessary to transform our `fake_header` object into a dictionary representation that is compatible with the __request library__. For this purpose, the `FakeHttpHeader` class provides the `as_header_dict` method.

```python
import requests

my_url = https://github.com/
fake_header_dict = fake_header.as_header_dict

r = requests.get(my_url, headers=fake_header_dict)
``` 

## Future ideas
 - Add weights to certain header fiels (e.g. __Accept: text/html, application/xhtml+xml, application/xml;**q=0.9**__)

## Contributing

Feel free to create pull requests and discuss some new to ideas to make the package more powerful.