---
layout: page
title: common/pamstretch (Nederlands)
description: "Vergroot een PAM afbeelding door te interpoleren tussen pixels."
content_hash: 3878776edbf6a885f20265cf92c7d243972f6328
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamstretch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamstretch

Vergroot een PAM afbeelding door te interpoleren tussen pixels.
Bekijk ook: `pamstretch-gen`, `pamenlarge`, `pamscale`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- Vergroot een PAM afbeelding met een gehele factor:

`pamstretch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Vergroot een PAM afbeelding met de gespecificeerde factoren in de horizontale en verticale richtingen:

`pamstretch -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
