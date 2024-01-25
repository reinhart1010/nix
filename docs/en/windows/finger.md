---
layout: page
title: windows/finger (English)
description: "Return information about users on a specified system."
content_hash: ebf34cd88c86708b70a01bbc30367ad2bd62e806
last_modified_at: 2024-01-25
related_topics:
  - title: 中文 version
    url: /zh/windows/finger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# finger

Return information about users on a specified system.
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
