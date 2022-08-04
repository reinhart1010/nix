---
layout: page
title: linux/lsns (English)
description: "List information about all namespaces or about the specified namespace."
content_hash: d65121d9a5c38c8ea54be0300d25ace1d59c26c5
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsns

List information about all namespaces or about the specified namespace.
More information: <https://man7.org/linux/man-pages/man8/lsns.8.html>.

- List all namespaces:

`lsns`

- List namespaces in JSON format:

`lsns --json`

- List namespaces associated with `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>`:

`lsns --task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- List the specified type of namespaces only:

`lsns --type <mnt|net|ipc|user|pid|uts|cgroup|time>`

- List namespaces, only showing the namespace ID, type, PID, and command:

`lsns --output NS,TYPE,PID,COMMAND`
