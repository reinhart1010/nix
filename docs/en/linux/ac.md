---
layout: page
title: linux/ac (English)
description: "Print statistics on how long users have been connected."
content_hash: e0114208d04afbf3a239a3d4a7359bdf0d9d9d84
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

Print statistics on how long users have been connected.
More information: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Print how long the current user has been connected in hours:

`ac`

- Print how long users have been connected in hours:

`ac --individual-totals`

- Print how long a particular user has been connected in hours:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Print how long a particular user has been connected in hours per day (with total):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Also display additional details:

`ac --compatibility`
