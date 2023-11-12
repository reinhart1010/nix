---
layout: page
title: common/ac (English)
description: "Print statistics on how long users have been connected."
content_hash: 660aa284f96ca8b33268d31efc9b7995d7bec29d
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

Print statistics on how long users have been connected.
More information: <https://man.openbsd.org/ac>.

- Print how long the current user has been connected in hours:

`ac`

- Print how long users have been connected in hours:

`ac -p`

- Print how long a particular user has been connected in hours:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Print how long a particular user has been connected in hours per day (with total):

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
