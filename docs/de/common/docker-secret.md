---
layout: page
title: common/docker-secret (Deutsch)
description: "Verwalte Secrets für Docker Swarm."
content_hash: e213d3159e43096c6ef665def7e4c250ed65b71b
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/docker-secret.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-secret.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-secret.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-secret.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker secret

Verwalte Secrets für Docker Swarm.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/secret/>.

- Erstelle ein neues Secret über die Standardeingabe:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` -`

- Erstelle ein neues Secret aus einer Datei:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Liste alle Secrets auf:

`docker secret ls`

- Zeige detaillierte Informationen zu einem oder mehreren Secrets in einem menschenlesbaren Format:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name1 secret_name2 ...</span>

- Lösche eines oder mehrere Secrets:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name1 secret_name2 ...</span>
