---
layout: page
title: common/nproc (English)
description: "Print the number of processing units (normally CPUs) available."
content_hash: 079a334cdf4f6750099136ece815fcfcb6ddecfb
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/nproc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nproc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nproc

Print the number of processing units (normally CPUs) available.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/nproc-invocation.html>.

- Display the number of available processing units:

`nproc`

- Display the number of installed processing units, including any inactive ones:

`nproc --all`

- If possible, subtract a given number of units from the returned value:

`nproc --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
