---
layout: page
title: common/kill (français)
description: "Envoie un signal à un processus, généralement pour l'interrompre."
content_hash: 131c0959ff4b556b284a03948714e0be4381dbd2
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kill.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kill

Envoie un signal à un processus, généralement pour l'interrompre.
Tous les signaux sauf SIGKILL et SIGSTOP peuvent être interceptés par le processus pour pouvoir se terminer proprement.
Plus d'informations : <https://manned.org/kill>.

- Termine un processus avec le signal SIGTERM (terminaison) par défaut :

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indentifiant_processus</span>

- Liste les noms des signaux disponibles (à utiliser sans leurs préfixes `SIG`) :

`kill -l`

- Termine une tâche de fond :

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_tâche</span>

- Termine un processus avec le signal SIGHUP ("raccrocher"). Beaucoup de daemons se rafraîchissent au lieu de terminer :

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indentifiant_processus</span>

- Termine un processus avec le signal SIGINT ("interruption"). Généralement initié par l'utilisateur appuyant sur `Ctrl + C` :

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indentifiant_processus</span>

- Demande au système d'exploitation de mettre fin à un processus immédiatement (sans possibilité d'intercepter le signal) :

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indentifiant_processus</span>

- Demande au système d'exploitation de suspendre un processus jusqu'à recevoir le signal SIGCONT ("continue") :

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indentifiant_processus</span>

- Envoie le signal SIGUSR1 à tous les processus dans le groupe avec l'identifiant indiqué :

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_groupe</span>
