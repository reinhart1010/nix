---
layout: page
title: common/age (français)
description: "Un outil de cryptage de fichiers simple, moderne et sécurisé."
content_hash: 448455b6a1cacda19581540b11b5d380c9c35274
last_modified_at: 2023-12-20
related_topics:
  - title: Deutsch version
    url: /de/common/age.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/age.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/age.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/age.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/age.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/age.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># age

Un outil de cryptage de fichiers simple, moderne et sécurisé.
Plus d'informations : <https://github.com/FiloSottile/age>.

- Générez un fichier crypté qui peut être décrypté avec une mot de passe :

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_crypté</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_non_crypté</span>

- Générer une paire de clés, en enregistrant la clé privée dans un fichier non crypté et en imprimant la clé publique sur `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Cryptage d'un fichier avec une ou plusieurs clés publiques qui sont entrées comme des littéraux :

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clé_publique_1</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clé_publique_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_non_crypté</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_crypté</span>

- Cryptez un fichier avec une ou plusieurs clés publiques spécifiées dans un fichier de destinataires :

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_destinataire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_non_crypté</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_crypté</span>

- Déchiffrer un fichier avec un mot de passe :

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_décrypté</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_crypté</span>

- Decrypt a file with a private key file :

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_clé_privée</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_décrypté</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_crypté</span>
