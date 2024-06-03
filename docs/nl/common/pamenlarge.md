---
layout: page
title: common/pamenlarge (Nederlands)
description: "Vergroot een PAM afbeelding door de pixels te dupliceren."
content_hash: 6c3e4d11fe830460fbb1c30d91a73a44ace7ece2
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamenlarge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamenlarge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamenlarge

Vergroot een PAM afbeelding door de pixels te dupliceren.
Bekijk ook: `pbmreduce`, `pamditherbw`, `pbmpscale`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamenlarge.html>.

- Vergroot de gespecificeerde afbeelding met de gespecificeerde factor:

`pamenlarge -scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Vergroot de gespecificeerde afbeelding met de gespecificeerde factors horizontaal en verticaal:

`pamenlarge -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
