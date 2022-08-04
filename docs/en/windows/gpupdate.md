---
layout: page
title: windows/gpupdate (English)
description: "A tool to check and apply Windows Group Policy settings."
content_hash: 59fcccffde4462b2c3227ba3d91a7127d46d3d7d
---
# gpupdate

A tool to check and apply Windows Group Policy settings.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- Check and apply updated Group Policy settings:

`gpupdate`

- Specify the target Group Policy settings to check for update:

`gpupdate /target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer|user</span>

- Force all Group Policy settings to be reapplied:

`gpupdate /force`

- Display detailed usage information:

`gpupdate /?`
