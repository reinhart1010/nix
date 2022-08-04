---
layout: page
title: common/git-am (italiano)
description: "Applica file di patch. Utile quando si ricevono commit via email."
content_hash: a33cbc92eddebd37308c84e9811721bea9506e06
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
---
# git am

Applica file di patch. Utile quando si ricevono commit via email.
Vedi anche `git format-patch` per generare file di patch.
Maggiori informazioni: <https://git-scm.com/docs/git-am>.

- Applica un file di patch:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.patch</span>

- Interrompi l'applicazione di un file di patch:

`git am --abort`

- Applica quanto possibile di un file di patch, salvando le parti non applicabili in file `.rej`:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.patch</span>
