---
layout: page
title: common/ac (français)
description: "Imprime les statistiques sur combien de temps les utilisateurs ont été connectés."
content_hash: 91d3434f45a22552d7443d88ad1e641fdcafb19a
last_modified_at: 2023-11-18
related_topics:
  - title: বাংলা version
    url: /bn/common/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ac

Imprime les statistiques sur combien de temps les utilisateurs ont été connectés.
Plus d'informations : <https://man.openbsd.org/ac>.

- Imprime combien de temps l'utilisateur actuel a été connecté en heures :

`ac`

- Imprime combien de temps les utilisateurs ont été connecté :

`ac -p`

- Imprime combien de temps un utilisateur en particulier a été connecté en heures :

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>

- Imprime combien de temps un utilisateur particulier a été connecté en heure par jour (avec le total) :

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>
