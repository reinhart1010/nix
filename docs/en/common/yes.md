---
layout: page
title: common/yes (English)
description: "Output something repeatedly."
content_hash: 8c112262abd1585f7493277de771cc3195a8527d
last_modified_at: 2024-02-12
related_topics:
  - title: español version
    url: /es/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yes

Output something repeatedly.
This command is commonly used to answer yes to every prompt by install commands (such as apt-get).
More information: <https://www.gnu.org/software/coreutils/yes>.

- Repeatedly output "message":

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Repeatedly output "y":

`yes`

- Accept everything prompted by the `apt-get` command:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Repeatedly output a newline to always accept the default option of a prompt:

`yes ''`
