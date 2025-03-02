---
layout: page
title: linux/runcon (English)
description: "Run a program in a different SELinux security context."
content_hash: 367491aa6ae8ba3d3b0254a8380847e66cf5dc35
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/runcon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/runcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runcon

Run a program in a different SELinux security context.
See also: `secon`.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- Print the security context of the current execution context:

`runcon`

- Specify the domain to run a command in:

`runcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify the context role to run a command with:

`runcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>`_r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify the full context to run a command with:

`runcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`_u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>`_r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
