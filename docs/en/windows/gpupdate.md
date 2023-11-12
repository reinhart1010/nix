---
layout: page
title: windows/gpupdate (English)
description: "A tool to check and apply Windows Group Policy settings."
content_hash: 23bbf445f326cc39d72df1267a6a2f44f3b1e250
last_modified_at: 2023-11-12
related_topics:
  - title: svenska version
    url: /sv/windows/gpupdate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpupdate

A tool to check and apply Windows Group Policy settings.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- Check and apply updated Group Policy settings:

`gpupdate`

- Specify the target Group Policy settings to check for update:

`gpupdate /target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer|user</span>

- Force all Group Policy settings to be reapplied:

`gpupdate /force`

- Display detailed usage information:

`gpupdate /?`
