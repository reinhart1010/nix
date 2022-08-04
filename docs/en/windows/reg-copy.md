---
layout: page
title: windows/reg-copy (English)
description: "Copy keys and their values in the registry."
content_hash: 4c349a85cbdf8785d2bbe6830aa6cd312a418c4f
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-copy.html
    icon: bi bi-globe
---
# reg copy

Copy keys and their values in the registry.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- Copy a registry key to a new registry location:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>

- Copy a registry key recursively to a new registry location:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>` /s`

- Forcefully copy a registry key without a prompt:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>` /f`
