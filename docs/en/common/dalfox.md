---
layout: page
title: common/dalfox (English)
description: "A powerful open-source XSS scanner focused on automation."
content_hash: c132c1adb599fb33777bf94595a3722da6c9cd8e
last_modified_at: 2023-11-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dalfox.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dalfox

A powerful open-source XSS scanner focused on automation.
More information: <https://dalfox.hahwul.com/docs/usage>.

- Scan a single URL for XSS vulnerabilities:

`dalfox url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Scan a URL using a header for authentication:

`dalfox url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-My-Header: 123'</span>

- Scan a list of URLs from a file:

`dalfox file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
