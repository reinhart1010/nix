---
layout: page
title: common/act (English)
description: "Execute GitHub Actions locally using Docker."
content_hash: b6388a6226a8f316436effa6c76b4e4fc5b16ba0
last_modified_at: 2023-12-03
related_topics:
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 2
---
# act

Execute GitHub Actions locally using Docker.
More information: <https://github.com/nektos/act>.

- [l]ist the available actions:

`act -l`

- Run the default event:

`act`

- Run a specific event:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>

- Run a specific [a]ction:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- Do [n]ot actually run the actions (i.e. a dry run):

`act -n`

- Show [v]erbose logs:

`act -v`

- Run a specific [W]orkflow:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/workflow</span>
