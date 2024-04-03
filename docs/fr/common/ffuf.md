---
layout: page
title: common/ffuf (français)
description: "Un outil d'énumération web rapide écrit en Go."
content_hash: a88484eb3e56e762a06da7bf94631a2dbcb15e00
last_modified_at: 2024-04-03
related_topics:
  - title: English version
    url: /en/common/ffuf.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ffuf

Un outil d'énumération web rapide écrit en Go.
Le mot-clé `FUZZ` est utilisé comme substitut. `ffuf` essaiera d'atteindre l'URL en remplaçant le mot `FUZZ` par tous les mots de la liste donnée.
Plus d'informations : <https://github.com/ffuf/ffuf#usage>.

- Énumère les répertoires en utilisant une sortie [c]olorée et une liste ([w]ordlist) spécifiant une [u]RL cible :

`ffuf -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/liste.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://cible/FUZZ</span>

- Énumère les sous-domaines en changeant la position du mot-clé :

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sous-domaines.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://FUZZ.cible.com</span>

- Énumère avec le nombre de fils d'exécution ([t]hreads) spécifié (par défaut : 40) et passe le trafic par un serveur mandataire (pro[x]y) et sauvegarde la sortie ([o]utput) dans un fichier :

`ffuf -o -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/liste.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://cible/FUZZ</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>

- Énumère dans un en-tête ([H]eader) spécifique ("Nom : Valeur") et n'affiche que les [c]odes d'état HTTP correspondant ([m]atch) :

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/liste.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://cible.com</span>` -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Host: FUZZ</span>`" -mc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- Énumère en spécifiant une méthode HTTP spécifiée et des [d]onnées, tout en [f]iltrant les [c]odes d'état séparés par des virgules :

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/postdata.txt</span>` -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username=admin\&password=FUZZ</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://cible/login.php</span>` -fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">401,403</span>
