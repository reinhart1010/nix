---
layout: page
title: common/dalfox (English)
description: "A powerful open-source XSS scanner focused on automation."
content_hash: c132c1adb599fb33777bf94595a3722da6c9cd8e
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# dalfox

A powerful open-source XSS scanner focused on automation.
More information: <https://dalfox.hahwul.com/docs/usage>.

- Scan a single URL for XSS vulnerabilities:

`dalfox url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Scan a URL using a header for authentication:

`dalfox url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-My-Header: 123'</span>

- Scan a list of URLs from a file:

`dalfox file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
