---
layout: page
title: common/xh (English)
description: "Friendly and fast tool for sending HTTP requests."
content_hash: 785cf8eed908fc213c20b16cbec9bd604330fa80
last_modified_at: 2024-09-13
tldri18n_status: 2
---
# xh

Friendly and fast tool for sending HTTP requests.
Note: `xh`, written in rust, serves as an effective drop-in replacement for `http`.
See also: `http`, `curl`.
More information: <https://github.com/ducaale/xh>.

- Send a GET request:

`xh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>

- Send a POST request with a JSON body (key-value pairs are added to a top-level JSON object - e.g. `{"name": "john", "age": 25}`):

`xh post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=john</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">age:=25</span>

- Send a GET request with query parameters (e.g. `first_param=5&second_param=true`):

`xh get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_param==5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_param==true</span>

- Send a GET request with a custom header:

`xh get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header-name:header-value</span>

- Make a GET request and save the response body to a file:

`xh --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/json</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show equivalent `curl` command (this will not send any request):

`xh --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">curl|curl-long</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--follow --verbose get http://example.com user-agent:curl</span>
