---
layout: page
title: windows/wmic (English)
description: "Interactive shell for detailed information about running processes."
content_hash: f66f7e2308db70d1dead40f581efe050bd73500e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wmic

Interactive shell for detailed information about running processes.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- Fundamental grammar:

`wmic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">where_clause</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verb_clause</span>

- Show brief details about the currently running processes:

`wmic process list brief`

- Show full details about the currently running processes:

`wmic process list full`

- Access specific fields such as process name, process ID and parent process ID:

`wmic process get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name,processid,parentprocessid</span>

- Display information about a specific process:

`wmic process where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name="example.exe"</span>` list full`

- Display specific fields for a specific process:

`wmic process where processid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name,commandline</span>

- Kill a process:

`wmic process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` delete`
