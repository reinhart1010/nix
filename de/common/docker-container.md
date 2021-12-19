---
layout: page
title: common/docker-container (Deutsch)
description: "Verwalte Docker Container."
content_hash: 80cf6c2db9f567e966be5183047ec587249e872b
related_topics:
  - title: English version
    url: /en/common/docker-container.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-container.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-container.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-container.html
    icon: bi bi-globe
---
# docker container

Verwalte Docker Container.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/container/>.

- Liste zur Zeit laufende Container auf:

`docker container ls`

- Starte einen oder mehrere gestoppte Container:

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container2_name</span>

- Beende einen oder mehrere laufende Container sofort:

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Stoppe einen oder mehrere laufende Container:

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Pausiere alle Prozesse in einem oder mehreren Containern:

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Zeige detaillierte Informationen zu einem oder mehreren Containern an:

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Exportiere das Dateisystem eines Containers als tar Archiv:

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Erstelle ein neues Image aus den Änderungen eines Containers:

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
