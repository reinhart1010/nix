---
layout: page
title: windows/reg-copy (English)
description: "Copy keys and their values in the registry."
content_hash: 75f88b4857feb27260401993ffa473e6e81eb4a7
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg copy

Copy keys and their values in the registry.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- Copy a registry key to a new registry location:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>

- Copy a registry key recursively (with all [s]ubkeys) to a new registry location:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>` /s`

- [f]orcefully (without a prompt) copy a registry key:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>` /f`
