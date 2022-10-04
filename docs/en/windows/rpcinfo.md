---
layout: page
title: windows/rpcinfo (English)
description: "List programs via RPC on remote computers."
content_hash: 53552822d451ce90524bed804667decfb9011f18
---
# rpcinfo

List programs via RPC on remote computers.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- List all programs registered on the local computer:

`rpcinfo`

- List all programs registered on a remote computer:

`rpcinfo /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>

- Call a specific program on a remote computer using TCP:

`rpcinfo /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_name</span>

- Call a specific program on a remote computer using UDP:

`rpcinfo /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_name</span>
