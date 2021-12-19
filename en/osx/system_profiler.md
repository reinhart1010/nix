---
layout: page
title: osx/system_profiler (English)
description: "Report system hardware and software configuration."
content_hash: 2570a923233297b0055bb7cc0f7ea055586da0a1
related_topics:
  - title: 中文 version
    url: /zh/osx/system_profiler.html
    icon: bi bi-globe
---
# system_profiler

Report system hardware and software configuration.
More information: <https://ss64.com/osx/system_profiler.html>.

- Display a full system profiler report which can be opened by System Profiler.app:

`system_profiler -xml > MyReport.spx`

- Display a hardware overview (Model, CPU, Memory, Serial, etc):

`system_profiler SPHardwareDataType`

- Print the system serial number:

`system_profiler SPHardwareDataType|grep "Serial Number (system)" |awk '{print $4}'`
