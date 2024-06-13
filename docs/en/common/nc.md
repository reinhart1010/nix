---
layout: page
title: common/nc (English)
description: "Redirect I/O into a network stream through this versatile tool."
content_hash: 4b827aa7a41836b104e66fe8a6384b83e25a5466
last_modified_at: 2024-06-13
related_topics:
  - title: español version
    url: /es/common/nc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nc

Redirect I/O into a network stream through this versatile tool.
More information: <https://manned.org/nc.1>.

- Start a listener on the specified TCP port and send a file into it:

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Connect to a target listener on the specified port and receive a file from it:

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">received_filename</span>

- Scan the open TCP ports of a specified host:

`nc -v -z -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout_in_seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_port</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_port</span>

- Start a listener on the specified TCP port and provide your local shell access to the connected party (this is dangerous and can be abused):

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_executable</span>

- Connect to a target listener and provide your local shell access to the remote party (this is dangerous and can be abused):

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_executable</span>

- Act as a proxy and forward data from a local TCP port to the given remote host:

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Send an HTTP GET request:

`echo -e "GET / HTTP/1.1\nHost: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`\n\n" | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` 80`
