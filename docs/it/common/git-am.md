---
layout: page
title: common/git-am (italiano)
description: "Applica file di patch. Utile quando si ricevono commit via email."
content_hash: 1d373a01b86c12cf9d54b97ae044a9128111527d
last_modified_at: 2023-11-12
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
  - title: 한국어 version
    url: /ko/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git am

Applica file di patch. Utile quando si ricevono commit via email.
Vedi anche `git format-patch` per generare file di patch.
Maggiori informazioni: <https://git-scm.com/docs/git-am>.

- Applica un file di patch:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.patch</span>

- Interrompi l'applicazione di un file di patch:

`git am --abort`

- Applica quanto possibile di un file di patch, salvando le parti non applicabili in file `.rej`:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.patch</span>
