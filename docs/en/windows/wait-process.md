---
layout: page
title: windows/wait-process (English)
description: "Waits for the processes to be stopped before accepting more input."
content_hash: 517a5fa7c5494ae6aba71131719c87110286c2c4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Wait-Process

Waits for the processes to be stopped before accepting more input.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- Stop a process and wait:

`Stop-Process -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>`; Wait-Process -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Wait for processes for a specified time:

`Wait-Process -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` -Timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
