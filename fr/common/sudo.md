---
layout: page
title: common/sudo (français)
description: "Exécute une commande unique en tant que super-utilisateur (super-user) ou un autre utilisateur."
content_hash: e1018046c443a058c4dac9be0bc5bc8cdc949d57
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/sudo.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sudo.html
    icon: bi bi-globe
---
# sudo

Exécute une commande unique en tant que super-utilisateur (super-user) ou un autre utilisateur.
Plus d'informations : <https://www.sudo.ws/sudo.html>.

- Exécute une commande en tant que super-utilisateur :

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Édite un fichier en tant que super-utilisateur avec votre éditeur par défaut :

`sudo --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Exécute une commande en tant qu'un autre utilisateur et/ou groupe :

`sudo --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` --group=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- Répéte la dernière commande préfixée de `sudo` (uniquement dans `bash`, `zsh`, etc.) :

`sudo !!`

- Lance le terminal par défaut avec des privilèges de super-utilisateur et exécuter des fichiers à profil spécifique (`.profile`, `.bash_profile`, etc.) :

`sudo --login`

- Lance le terminal par défaut avec des privilèges de super-utilisateur sans modifier l'environnement :

`sudo --shell`

- Lance le terminal par défaut en tant que l'utilisateur spécifié, en chargeant l'environnement de cet utilisateur et en lisant les fichiers à profil spécifique de cet utilisateur (`.profile`, `.bash_profile`, etc.) :

`sudo --login --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Liste les commandes autorisées (et interdites) pour l'utilisateur courant :

`sudo --list`
