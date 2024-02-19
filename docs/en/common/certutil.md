---
layout: page
title: common/certutil (English)
description: "Manage keys and certificates in both NSS databases and other NSS tokens."
content_hash: 428826ec2f1c5469c06c8ff8dec2082c2c617aa4
last_modified_at: 2024-02-19
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

Manage keys and certificates in both NSS databases and other NSS tokens.
More information: <https://manned.org/certutil>.

- Create a [N]ew certificate database in the current [d]irectory:

`certutil -N -d .`

- List all certificates in a database:

`certutil -L -d .`

- List all private [K]eys in a database specifying the password [f]ile:

`certutil -K -d . -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file.txt</span>

- [A]dd the signed certificate to the requesters database specifying a [n]ickname, [t]rust attributes and an [i]nput CRT file:

`certutil -A -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_certificate</span>`" -t ",," -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.crt</span>` -d .`

- Add subject alternative names to a given [c]ertificate with a specific key size ([g]):

`certutil -S -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file.txt</span>` -d . -t ",," -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_certificate</span>`" -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>`" -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -s "CN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">common_name</span>`,O=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>`"`
