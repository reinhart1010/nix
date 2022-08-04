---
layout: page
title: windows/systeminfo (English)
description: "Display operating system configuration for a local or remote machine."
content_hash: 9b129fcefaee36849ea27b9ebf84cfa883ff58ee
related_topics:
  - title: 中文 version
    url: /zh/windows/systeminfo.html
    icon: bi bi-globe
---
# systeminfo

Display operating system configuration for a local or remote machine.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- Display system configuration for the local machine:

`systeminfo`

- Display system configuration in a specified output format:

`systeminfo /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Display system configuration for a remote machine:

`systeminfo /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Display detailed usage information:

`systeminfo /?`
