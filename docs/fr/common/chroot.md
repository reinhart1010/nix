---
layout: page
title: common/chroot (français)
description: "Exécute une commande ou un shell interactif avec un répertoire racine spécial."
content_hash: 6206cc5f180871b9eff3a8a26cbeaaced92e69a9
last_modified_at: 2024-12-12
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chroot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chroot.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chroot

Exécute une commande ou un shell interactif avec un répertoire racine spécial.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Exécute la commande en tant que nouveau répertoire racine :

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/nouveau/répertoire/racine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Spécifie l'utilisateur et le groupe (ID ou nom) à utiliser :

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur:groupe</span>
