---
layout: page
title: common/chromium (français)
description: "Navigateur Web open source principalement développé et maintenu par Google."
content_hash: da6f4956795f754cd04ba534fdf4a3e1996abc39
related_topics:
  - title: Deutsch version
    url: /de/common/chromium.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chromium.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chromium.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chromium.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chromium.html
    icon: bi bi-globe
---
# chromium

Navigateur Web open source principalement développé et maintenu par Google.
Plus d'informations : <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Ouvre une URL ou un fichier spécifique :

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemple.com|chemin/vers/fichier.html</span>

- Ouvre en mode navigation privée :

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>

- Ouvre dans une nouvelle fenêtre :

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>

- Ouvre en mode application (sans barres d'outils, barre d'URL, boutons, etc) :

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemple.com</span>

- Utilise un serveur proxy :

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>

- Ouvre dans un répertoire de profil personnalisé :

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Ouvre sans validation CORS (utile pour tester une API) :

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>` --disable-web-security`

- Ouvre avec une fenêtre outils de développement pour chaque onglet ouvert :

`chromium --auto-open-devtools-for-tabs`
