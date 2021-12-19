---
layout: page
title: windows/doskey (English)
description: "Manage macros, windows commands and command-lines."
content_hash: 24339f0f9d66aa7417677b8492037ec0b801410d
related_topics:
  - title: 中文 version
    url: /zh/windows/doskey.html
    icon: bi bi-globe
---
# doskey

Manage macros, windows commands and command-lines.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/doskey>.

- List available macros:

`doskey /macros`

- Create a new macro:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Create a new macro for a specific executable:

`doskey /exename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Remove a macro:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` =`

- Display all commands that are stored in memory:

`doskey /history`

- Save macros to a file for portability:

`doskey /macros > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macinit</span>

- Load macros from a file:

`doskey /macrofile = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macinit</span>
