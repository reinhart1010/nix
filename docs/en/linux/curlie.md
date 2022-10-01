---
layout: page
title: linux/curlie (English)
description: "Curlie is a frontend to curl that adds the ease of use of httpie."
content_hash: 52c2c58d9f720a560861be8a0280716815a353e3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># curlie

Curlie is a frontend to curl that adds the ease of use of httpie.
More information: <https://github.com/rs/curlie>.

- Send a GET request:

`curlie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>

- Send a POST request:

`curlie post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=john</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">age:=25</span>

- Send a GET request with query parameters (e.g. `first_param=5&second_param=true`):

`curlie get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_param==5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_param==true</span>

- Send a GET request with a custom header:

`curlie get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header-name:header-value</span>
