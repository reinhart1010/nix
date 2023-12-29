---
layout: page
title: common/ssh-keygen (français)
description: "Génère des clés SSH. Utilisées entre autres pour l'authentification ou la connexion sans utiliser de mot de passe."
content_hash: 24b460a0609f02d88278888ec575dec635a2bb94
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keygen.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keygen.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ssh-keygen

Génère des clés SSH. Utilisées entre autres pour l'authentification ou la connexion sans utiliser de mot de passe.
Plus d'informations : <https://man.openbsd.org/ssh-keygen>.

- Génère une clé de manière interactive :

`ssh-keygen`

- Génère une clé ed25519, avec 32 passages de fonction de dérivation de clé et enrigster dans un fichier spécifique :

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/fichier</span>

- Génère une clé RSA de 4096 bits, avec l'adresse électronique en commentaire :

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commentaire|email</span>`"`

- Retire les clés d'une machine donnée du fichier `known_hosts` des hôtes connus (utile lorsque un hôte déjà enregistré change de clé) :

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>

- Affiche l'empreinte d'une clé sous format d'un hash MD5 :

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/fichier</span>

- Change le mot de passe d'une clé :

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/fichier</span>

- Change le format d'une clé (par exemple du format OPENSSH vers PEM), le fichier étant réécrit :

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/cle_privee_OpenSSH</span>
