---
layout: page
title: osx/system_profiler (English)
description: "Report system hardware and software configuration."
content_hash: a93b1357000799e81ecea9703644a57da309af40
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/osx/system_profiler.html
    icon: bi bi-globe
tldri18n_status: 2
---
# system_profiler

Report system hardware and software configuration.
More information: <https://ss64.com/osx/system_profiler.html>.

- Display a report with specific details level (mini [no personal information], basic or full):

`system_profiler -detailLevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>

- Display a full system profiler report which can be opened by `System Profiler.app`:

`system_profiler -xml > MyReport.spx`

- Display a hardware overview (Model, CPU, Memory, Serial, etc) and software data (System, Kernel, Name, Uptime, etc):

`system_profiler SPHardwareDataType SPSoftwareDataType`

- Print the system serial number:

`system_profiler SPHardwareDataType|grep "Serial Number (system)" | awk '{ print $4 }'`
