---
layout: page
title: common/fc (English)
description: "Open the most recent command for editing and then run it."
content_hash: 23ea7906fc929502e3cc8a7de4e8eacd7ffc31b0
last_modified_at: 2024-10-07
related_topics:
  - title: Nederlands version
    url: /nl/common/fc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc

Open the most recent command for editing and then run it.
More information: <https://manned.org/fc>.

- Open the last command in the default system editor and run it after editing:

`fc`

- Specify an editor to open with:

`fc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'emacs'</span>

- List recent commands from history:

`fc -l`

- List recent commands in reverse order:

`fc -l -r`

- Edit and run a command from history:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Edit commands in a given interval and run them:

`fc '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">416</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">420</span>`'`

- Display help:

`fc --help`
