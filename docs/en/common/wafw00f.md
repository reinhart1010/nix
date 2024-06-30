---
layout: page
title: common/wafw00f (English)
description: "Identify and fingerprint Web Application Firewall (WAF) products protecting a website."
content_hash: 5b11eca4a537337d0b9b11c0daf78decfee06d3a
last_modified_at: 2024-06-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wafw00f.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wafw00f

Identify and fingerprint Web Application Firewall (WAF) products protecting a website.
More information: <https://github.com/EnableSecurity/wafw00f>.

- Check if a website is using any WAF:

`wafw00f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- Test for [a]ll detectable WAFs without stopping at the first match:

`wafw00f --findall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- Pass requests through a [p]roxy (such as BurpSuite):

`wafw00f --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- [t]est for a specific WAF product (run `wafw00f -l` to get list of all supported WAFs):

`wafw00f --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Cloudflare|Cloudfront|Fastly|ZScaler|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- Pass custom [H]eaders from a file:

`wafw00f --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/headers.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- Read target [i]nputs from a file and show verbose output (multiple `v` for more verbosity):

`wafw00f --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/urls.txt</span>` -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v</span>

- [l]ist all WAFs that can be detected:

`wafw00f --list`
