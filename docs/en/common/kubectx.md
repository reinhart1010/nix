---
layout: page
title: common/kubectx (English)
description: "Utility to manage and switch between `kubectl` contexts."
content_hash: 7da78ef081a87ab9bff816d9e20a8e8c14133548
last_modified_at: 2024-06-12
related_topics:
  - title: ไทย version
    url: /th/common/kubectx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectx

Utility to manage and switch between `kubectl` contexts.
More information: <https://github.com/ahmetb/kubectx>.

- List the contexts:

`kubectx`

- Switch to a named context:

`kubectx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Switch to the previous context:

`kubectx -`

- Rename a named context:

`kubectx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Show the current named context:

`kubectx -c`

- Delete a named context:

`kubectx -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
