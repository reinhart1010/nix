---
layout: page
title: common/pamflip (Nederlands)
description: "Flip of draai een PAM of PNM afbeelding."
content_hash: cc4fe6723f53208505bb33fa56d604f346eaa0a2
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamflip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamflip

Flip of draai een PAM of PNM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Draai de invoer-afbeelding tegen de klok in met de gespecificeerde graden::

`pamflip -rotate`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90|180|270</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Flip links met rechts:

`pamflip -leftright `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Flip boven met onder:

`pamflip -topbottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Flip de invoer-afbeelding met de diagonaal:

`pamflip -transpose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
