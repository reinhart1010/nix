---
layout: page
title: common/cfssl (English)
description: "Cloudflare's PKI and TLS toolkit."
content_hash: 0854207cfe692dc8a84711762a6564aa53fd7e97
last_modified_at: 2024-10-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cfssl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cfssl

Cloudflare's PKI and TLS toolkit.
See also: `openssl`.
More information: <https://github.com/cloudflare/cfssl>.

- Show certificate information of a host:

`cfssl certinfo -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.google.com</span>

- Decode certificate information from a file:

`cfssl certinfo -cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate.pem</span>

- Scan host(s) for SSL/TLS issues:

`cfssl scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1 host2 ...</span>

- Display help for a subcommand:

`cfssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">genkey|gencsr|certinfo|sign|gencrl|ocspdump|ocsprefresh|ocspsign|ocspserve|scan|bundle|crl|print-defaults|revoke|gencert|serve|version|selfsign|info</span>` -h`
