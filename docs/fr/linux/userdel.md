---
layout: page
title: linux/userdel (français)
description: "Supprime un compte utilisateur ou supprime un utilisateur d'un groupe."
content_hash: 80920f5b26c22c12f42bbb4d39701674d1f3a9a7
last_modified_at: 2022-12-30
related_topics:
  - title: català version
    url: /ca/linux/userdel.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/userdel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># userdel

Supprime un compte utilisateur ou supprime un utilisateur d'un groupe.
Voir aussi `users`, `useradd`, `usermod`.
Plus d'informations : <https://manned.org/userdel>.

- Supprime un utilisateur :

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Supprime un utilisateur dans un autre répertoire racine :

`sudo userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/autre_racine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Supprime un utilisateur, son répertoire personnel ainsi que son répertoire d'attente des courriels :

`sudo userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>
