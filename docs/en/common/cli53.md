---
layout: page
title: common/cli53 (English)
description: "Command line tool for Amazon Route 53."
content_hash: 49c6f43037ec9fc73f5ef6cfec6a367432fac938
last_modified_at: 2023-11-03
---
# cli53

Command line tool for Amazon Route 53.
More information: <https://github.com/barnybug/cli53>.

- List domains:

`cli53 list`

- Create a domain:

`cli53 create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mydomain.com</span>` --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comment</span>`"`

- Export a bind zone file to `stdout`:

`cli53 export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mydomain.com</span>

- Create a `www` subdomain pointing to a relative record in the same zone:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mydomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 CNAME lb'</span>

- Create a `www` subdomain pointing to an external address (must end with a dot):

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mydomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 CNAME lb.externalhost.com.'</span>

- Create a `www` subdomain pointing to an IP address:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mydomain.com} `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 A 150.130.110.1'</span>

- Replace a `www` subdomain pointing to a different IP:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 A 150.130.110.2'</span>

- Delete a record A:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rd|rrdelete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mydomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A</span>
