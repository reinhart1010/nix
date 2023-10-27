---
layout: page
title: windows/psexec (English)
description: "Execute a command-line process on a remote machine."
content_hash: 031a06ddb571712ac93dd2a5a787d965106a0ec7
last_modified_at: 2023-10-27
---
# psexec

Execute a command-line process on a remote machine.
This is an advanced command and it might potentially be dangerous.
More information: <https://learn.microsoft.com/sysinternals/downloads/psexec>.

- Execute a command using `cmd` in a remote shell:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` cmd`

- Execute a command on a remote host (pre-authenticated):

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Execute a command remotely and output the result to a file:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -an ^>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.txt</span>

- Execute a program to interact with users:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` -d -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_name</span>

- Display the IP configuration of the remote host:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` ipconfig /all`
