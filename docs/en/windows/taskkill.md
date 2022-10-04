---
layout: page
title: windows/taskkill (English)
description: "Terminate a process by its process ID or name."
content_hash: c85a19b0fd674359e39daa60a31fd3be61e0648b
related_topics:
  - title: 中文 version
    url: /zh/windows/taskkill.html
    icon: bi bi-globe
---
# taskkill

Terminate a process by its process ID or name.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- Terminate a process by its ID:

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Terminate a process by its name:

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Forcefully terminate a specified process:

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>` /f`

- Terminate a process and its child processes:

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` /t`

- Terminate a process on a remote machine:

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Display information about the usage of the command:

`taskkill /?`
