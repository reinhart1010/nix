---
layout: page
title: common/nikto (English)
description: "Web server scanner which performs tests against web servers for multiple items."
content_hash: 68e6814c1d74c0f90e81aacb81795a65cedfcfcf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nikto

Web server scanner which performs tests against web servers for multiple items.
More information: <https://cirt.net/Nikto2>.

- Perform a basic Nikto scan against a target host:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>

- Specify the port number when performing a basic scan:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>

- Scan ports and protocols with full URL syntax:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://192.168.0.1:443/</span>

- Scan multiple ports in the same scanning session:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,88,443</span>

- Update to the latest plugins and databases:

`perl nikto.pl -update`
