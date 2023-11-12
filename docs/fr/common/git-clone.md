---
layout: page
title: common/git-clone (français)
description: "Clone un dépôt existant."
content_hash: 9282455832a2e6a1cac69446c48afe6c71e8742e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-clone.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-clone.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clone.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clone.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clone.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-clone.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-clone.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clone

Clone un dépôt existant.
Plus d'informations : <https://git-scm.com/docs/git-clone>.

- Clone un dépôt existant :

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>

- Clone un dépôt existant dans un répertoire spécifique :

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/repertoire</span>

- Clone un dépôt existant et ses sous-modules :

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>

- Clone un dépôt local :

`git clone -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/depot/local</span>

- Clone silencieusement :

`git clone -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>

- Clone un dépôt existant en ne récupérant que les 10 commits les plus récents sur la branche par défaut (plus rapide) :

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>

- Clone un dépôt existant en ne récupérant qu'une branche spécifique :

`git clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` --single-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>

- Clone un dépôt existant en utilisant une commande SSH spécifique :

`git clone --config core.sshCommand="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh -i chemin/vers/clef_ssh_privee</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emplacement_du_depot_distant</span>
