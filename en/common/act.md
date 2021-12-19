---
layout: page
title: common/act (English)
description: "Execute GitHub Actions locally using Docker."
content_hash: 9713eb1b49b6148fd38d738f14b1c267dae8c5d8
related_topics:
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
---
# act

Execute GitHub Actions locally using Docker.
More information: <https://github.com/nektos/act>.

- List the available actions:

`act -l`

- Run the default event:

`act`

- Run a specific event:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>

- Run a specific action:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- Do not actually run the actions (i.e. a dry run):

`act -n`

- Show verbose logs:

`act -v`
