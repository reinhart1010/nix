---
layout: page
title: linux/ncat (English)
description: "Read, write, redirect, and encrypt data across a network."
content_hash: b465a04cd8ec50b64d2ee5e60838bdf2505633b2
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# ncat

Read, write, redirect, and encrypt data across a network.
An alternative implementation of a similar utility called `netcat`/`nc`.
More information: <https://nmap.org/ncat/guide/index.html>.

- Listen for input on the specified port and write it to the specified file:

`ncat -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Accept multiple connections and keep ncat open after they have been closed:

`ncat -lk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Write output of specified file to the specified host on the specified port:

`ncat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Accept multiple incoming connections on an encrypted channel evading detection of traffic content:

`ncat --ssl -k -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Connect to an open `ncat` connection over SSL:

`ncat --ssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Check connectivity to a remote host on a particular port with timeout:

`ncat -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` -vz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
