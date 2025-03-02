---
layout: page
title: linux/chsh (English)
description: "Change user's login shell."
content_hash: 0b0efcb03171112fbe714f2e657f4e51b32a4793
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/chsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chsh

Change user's login shell.
Part of `util-linux`.
More information: <https://manned.org/chsh>.

- Set a specific login shell for the current user interactively:

`chsh`

- Set a specific login [s]hell for the current user:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Set a login [s]hell for a specific user:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
