---
layout: page
title: common/act (English)
description: "Execute GitHub Actions locally using Docker."
content_hash: a2fbdacbe2da359aa4b6205f32321874dc9d2144
last_modified_at: 2024-01-28
related_topics:
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/act.html
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

- [l]ist the available jobs:

`act -l`

- Run the default event:

`act`

- Run a specific event:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>

- Run a specific [j]ob:

`act -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Do [n]ot actually run the actions (i.e. a dry run):

`act -n`

- Show [v]erbose logs:

`act -v`

- Run a specific [W]orkflow with the push event:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/workflow</span>
