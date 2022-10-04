---
layout: page
title: windows/tasklist (English)
description: "Display a list of currently running processes on a local or remote machine."
content_hash: 47305d02e52d0f7c55d5f3477bd9519f41900911
related_topics:
  - title: 中文 version
    url: /zh/windows/tasklist.html
    icon: bi bi-globe
---
# tasklist

Display a list of currently running processes on a local or remote machine.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- Display currently running processes:

`tasklist`

- Display running processes in a specified output format:

`tasklist /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Display running processes using the specified `.exe` or `.dll` file name:

`tasklist /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_pattern</span>

- Display processes running on a remote machine:

`tasklist /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Display services using each process:

`tasklist /svc`
