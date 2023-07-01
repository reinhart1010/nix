---
layout: page
title: windows/w32tm (English)
description: "Query and control the w32time time synchronization service."
content_hash: 19da3052fbd7b83ac952b05570aee95d36b96878
last_modified_at: 2023-07-01
---
# w32tm

Query and control the w32time time synchronization service.
More information: <https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- Show the current status of time synchronization:

`w32tm /query /status /verbose`

- Show a time offset graph against a time server:

`w32tm /stripchart /computer:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_server</span>

- Show an NTP reply from a time server:

`w32tm /stripchart /packetinfo /samples:1 /computer:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_server</span>

- Show the state of the currently used time servers:

`w32tm /query /peers`

- Show configuration of the w32time service (run in elevated console):

`w32tm /query /configuration`

- Force time resynchronization immediately (run in elevated console):

`w32tm /resync /force`

- Write w32time debug logs into a file (run in elevated console):

`w32tm /debug /enable /file:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\debug.log</span>` /size:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000000</span>` /entries:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-300</span>
