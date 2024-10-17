---
layout: page
title: linux/aa-complain (Nederlands)
description: "Stel een AppArmor-profiel in op klaagmodus."
content_hash: 4ae9f0d6ef746aac1ba18b628a65a4144393a6b9
last_modified_at: 2024-10-17
related_topics:
  - title: Deutsch version
    url: /de/linux/aa-complain.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aa-complain.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-complain.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-complain

Stel een AppArmor-profiel in op klaagmodus.
Bekijk ook: `aa-disable`, `aa-enforce`, `aa-status`.
Meer informatie: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Stel een profiel in op klaagmodus:

`sudo aa-complain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/profiel1 pad/naar/profiel2 ...</span>

- Stel profielen in op klaagmodus:

`sudo aa-complain --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/profielen</span>
