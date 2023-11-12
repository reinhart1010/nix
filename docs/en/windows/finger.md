---
layout: page
title: windows/finger (English)
description: "Return information about one or more users on a specified system."
content_hash: 9c85f8d18e841ea48b9f58e977f58366b4bb5018
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/finger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# finger

Return information about one or more users on a specified system.
The remote system must be running the Finger service.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- Display information about a specific user:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Display information about all users on the specified host:

`finger @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Display information in a longer format:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -l`

- Display help information:

`finger /?`
