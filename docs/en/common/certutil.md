---
layout: page
title: common/certutil (English)
description: "Manage keys and certificates in both NSS databases and other NSS tokens."
content_hash: 2c72be7f50edd3e7266e917afa1521b80c947c1f
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># certutil

Manage keys and certificates in both NSS databases and other NSS tokens.
More information: <https://manned.org/certutil>.

- Create a new certificate database:

`certutil -N -d .`

- List all certificates in a database:

`certutil -L -d .`

- List all private keys in a database:

`certutil -K -d . -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pwdfile.txt</span>

- Import the signed certificate into the requesters database:

`certutil -A -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Server-cert</span>`" -t ",," -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.crt</span>` -d .`

- Add subject alternative names to a given certificate:

`certutil -S -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pwdfile.txt</span>` -d . -t ",," -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Server-Cert</span>`" -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server1</span>`" -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -s "CN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testuser1</span>`,O=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testrelm.test</span>`"`
