---
layout: page
title: common/chgrp (Nederlands)
description: "Verander beheerdersgroep van bestanden en mappen."
content_hash: 9141bb4b7e9a4d14bb69c4151f40d43f5a7f5046
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/chgrp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chgrp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chgrp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chgrp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chgrp

Verander beheerdersgroep van bestanden en mappen.
Meer informatie: <https://www.gnu.org/software/coreutils/chgrp>.

- Verander beheerdergroep van een bestand of map:

`chgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Verander recursief de beheerdersgroep van een map en alle bestanden erin:

`chgrp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Verander beheerdersgroep van een symbolische link:

`chgrp -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/symlink</span>

- Verander de beheerdersgroep van een bestand/map naar de permissies van een referentiebestand:

`chgrp --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/referentiebestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>
