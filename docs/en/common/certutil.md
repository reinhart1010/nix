---
layout: page
title: common/certutil (English)
description: "Manage keys and certificates in both NSS databases and other NSS tokens."
content_hash: 33fa023720f7c6d36d4a1b876c3d8845ceeca45b
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

Manage keys and certificates in both NSS databases and other NSS tokens.
More information: <https://manned.org/certutil>.

- Create a new certificate database:

`certutil -N -d .`

- List all certificates in a database:

`certutil -L -d .`

- List all private keys in a database:

`certutil -K -d . -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file.txt</span>

- Import the signed certificate into the requesters database:

`certutil -A -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_certificate</span>`" -t ",," -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.crt</span>` -d .`

- Add subject alternative names to a given certificate:

`certutil -S -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file.txt</span>` -d . -t ",," -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_certificate</span>`" -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>`" -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -s "CN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">common_name</span>`,O=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>`"`
