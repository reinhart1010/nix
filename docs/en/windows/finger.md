---
layout: page
title: windows/finger (English)
description: "Return information about one or more users on a specified system."
content_hash: 3c8092ad6d8f46def1cbf0d88b85365f18266902
related_topics:
  - title: 中文 version
    url: /zh/windows/finger.html
    icon: bi bi-globe
---
# finger

Return information about one or more users on a specified system.
The remote system must be running the Finger service.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/finger>.

- Display information about a specific user:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Display information about all users on the specified host:

`finger @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Display information in a longer format:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -l`

- Display help information:

`finger /?`
