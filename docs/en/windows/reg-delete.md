---
layout: page
title: windows/reg-delete (English)
description: "Delete keys or their values from the registry."
content_hash: d2acd42a9d21d46dc1579b84dbe1d36f4a38f5ff
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg-delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg delete

Delete keys or their values from the registry.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- Delete a specific registry key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Delete a [v]alue under a specific key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Delete [a]ll [v]alues recursively under the specified key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /va`

- [f]orcefully (without a prompt) delete [a]ll [v]alues recursively under a key:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` /f /va`
