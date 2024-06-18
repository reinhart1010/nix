---
layout: page
title: linux/lsns (English)
description: "List information about all namespaces or about the specified namespace."
content_hash: 849977ccf501a4e54694b87cf6031d1e915e63aa
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# lsns

List information about all namespaces or about the specified namespace.
More information: <https://manned.org/lsns>.

- List all namespaces:

`lsns`

- List namespaces in JSON format:

`lsns --json`

- List namespaces associated with the specified process:

`lsns --task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- List the specified type of namespaces only:

`lsns --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mnt|net|ipc|user|pid|uts|cgroup|time</span>

- List namespaces, only showing the namespace ID, type, PID, and command:

`lsns --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NS,TYPE,PID,COMMAND</span>
