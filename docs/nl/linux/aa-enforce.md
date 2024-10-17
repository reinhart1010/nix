---
layout: page
title: linux/aa-enforce (Nederlands)
description: "Stel een AppArmor-profiel in op afdwingmodus."
content_hash: 768de72674d1b8c8407bf0964b91a55ecba02415
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/linux/aa-enforce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-enforce

Stel een AppArmor-profiel in op afdwingmodus.
Bekijk ook: `aa-complain`, `aa-disable`, `aa-status`.
Meer informatie: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Schakel een profiel in:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/profiel1 pad/naar/profiel2 ...</span>

- Schakel profielen in:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/profiel</span>
