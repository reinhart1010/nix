---
layout: page
title: common/alias (français)
description: "Créé des alias -- mots qui sont remplacés par une commande textuelle."
content_hash: 3bf6b1299ede5177d6a9dc946c4725e2b776db68
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/alias.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/alias.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alias.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alias.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/alias.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/alias.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alias.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alias.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/alias.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alias.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/alias.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alias.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alias.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alias.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/alias.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/alias.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alias.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alias

Créé des alias -- mots qui sont remplacés par une commande textuelle.
Les alias expirent avec la session courante shell, sauf s'il a été défini dans le fichier de configuration shell, par exemple `~/.bashrc`.
Plus d'informations : <https://tldp.org/LDP/abs/html/aliases.html>.

- Liste tous les alias :

`alias`

- Crée un alias générique :

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`"`

- Affiche la commande associée à un alias donné :

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot</span>

- Enlève un alias :

`unalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot</span>

- Transforme `rm` en une commande intéractive :

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm -i</span>`"`

- Crée `la` comme un raccourci de `ls -a` :

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">la</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -a</span>`"`
