---
layout: page
title: windows/cmstp (English)
description: "A command-line tool for managing connection service profiles."
content_hash: 4c84a78c9b500e4bc3bced6d046fcf9e9cae3fd8
related_topics:
  - title: 中文 version
    url: /zh/windows/cmstp.html
    icon: bi bi-globe
---
# cmstp

A command-line tool for managing connection service profiles.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Install a specific profile:

`cmstp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Install without creating a desktop shortcut:

`cmstp /ns "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Install without checking for dependencies:

`cmstp /nf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Only install for the current user:

`cmstp /su "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Install for all users (requires administrator privileges):

`cmstp /au "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Install silently without any prompts:

`cmstp /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Uninstall a specific profile:

`cmstp /u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`

- Uninstall silently without a confirmation prompt:

`cmstp /u /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>`"`
