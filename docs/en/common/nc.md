---
layout: page
title: common/nc (English)
description: "Netcat is a versatile utility for working with TCP or UDP data."
content_hash: 430ae5da9fe1a8fd41a3a42f05f32cd864a0d28e
last_modified_at: 2023-04-12
related_topics:
  - title: español version
    url: /es/common/nc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nc.html
    icon: bi bi-globe
---
# nc

Netcat is a versatile utility for working with TCP or UDP data.
More information: <https://manned.org/man/nc.1>.

- Establish a TCP connection:

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Set a timeout:

`nc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout_in_seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipaddress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Scan the open TCP ports of a specified host:

`nc -v -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Listen on a specified TCP port and print any data received:

`nc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Keep the server up after the client detaches:

`nc -k -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Listen on a specified UDP port and print connection details and any data received:

`nc -u -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Act as proxy and forward data from a local TCP port to the given remote host:

`nc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Send a HTTP request:

`echo -e "GET / HTTP/1.1\nHost: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`\n\n" | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` 80`
