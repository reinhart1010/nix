---
layout: page
title: common/autossh (français)
description: "Lance, surveille et redémarre les connections SSH."
content_hash: f10d2da1aa2bf689a93619c6135ba45dca8b7fb8
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/autossh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autossh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autossh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autossh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/autossh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autossh

Lance, surveille et redémarre les connections SSH.
Reconnecte automatiquement pour garder le tunnel de transfert de port ouvert. Accepte toutes les options de SSH.
Plus d'informations : <https://www.harding.motd.ca/autossh>.

- Démarre une session SSH, redémarre quand le port échoue à renvoyer de la data :

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_surveillé</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande_ssh</span>`"`

- Fait suivre un port local vers un port distant, redémarre si nécessaire :

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_surveillé</span>` -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_local</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hôte</span>

- Diverge `autossh` en arrière plan avant de lancer SSH et n'ouvre pas de shell distant :

`autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_surveillé</span>` -N "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande_ssh</span>`"`

- Démarre en arrière plan, sans surveillance de port et à la place envoie des paquets SSH "keep-alive" toutes les 10 secondes pour détecter les échecs :

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande_ssh</span>`"`

- Démarre en arrière plan, sans surveillance de port ni shell distant et s’arrête si le partage de port échoue :

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_local</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hôte</span>

- Démarre en arrière plan, logue la sortie de déboggage d'`autossh` et la sortie verbeuse de SSH dans des fichiers :

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_logs_autossh.log</span>` autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_surveillé</span>` -v -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_logs_ssh.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande_ssh</span>
