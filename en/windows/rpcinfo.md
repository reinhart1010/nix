---
layout: page
title: windows/rpcinfo (English)
description: "List programs via RPC on remote computers."
content_hash: de211327f82f7fc57200f81286bc470b41c20559
---
# rpcinfo

List programs via RPC on remote computers.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- List all programs registered on the local computer:

`rpcinfo`

- List all programs registered on a remote computer:

`rpcinfo /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>

- Call a specific program on a remote computer using TCP:

`rpcinfo /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_name</span>

- Call a specific program on a remote computer using UDP:

`rpcinfo /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_name</span>
