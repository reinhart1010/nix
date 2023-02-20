---
layout: page
title: windows/reg-load (English)
description: "Load saved sub keys into a different sub key in the registry."
content_hash: 690421a75211f98b09a93750573509bb2b887035
last_modified_at: 2023-02-20
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-load.html
    icon: bi bi-globe
---
# reg load

Load saved sub keys into a different sub key in the registry.
This is intended for troubleshooting and temporary keys.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-load>.

- Load a backup file into the specified key:

`reg load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>
