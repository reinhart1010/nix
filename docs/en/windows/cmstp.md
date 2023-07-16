---
layout: page
title: windows/cmstp (English)
description: "Manage connection service profiles."
content_hash: 8b531de0173aed1be317bca02521411dd6deb715
last_modified_at: 2023-07-16
related_topics:
  - title: தமிழ் version
    url: /ta/windows/cmstp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmstp.html
    icon: bi bi-globe
---
# cmstp

Manage connection service profiles.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Install a specific profile:

`cmstp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Install without creating a desktop shortcut:

`cmstp /ns "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Install without checking for dependencies:

`cmstp /nf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Only install for the current user:

`cmstp /su "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Install for all users (requires administrator privileges):

`cmstp /au "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Install silently without any prompts:

`cmstp /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Uninstall a specific profile:

`cmstp /u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`

- Uninstall silently without a confirmation prompt:

`cmstp /u /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\profile_file</span>`"`
