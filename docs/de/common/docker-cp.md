---
layout: page
title: common/docker-cp (Deutsch)
description: "Kopiere Dateien oder Verzeichnisse zwischen Host- und Container-Dateisystem."
content_hash: e67e0405cda4841fadf500b9e0aad3fa78a13bab
related_topics:
  - title: English version
    url: /en/common/docker-cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-cp.html
    icon: bi bi-globe
---
# docker cp

Kopiere Dateien oder Verzeichnisse zwischen Host- und Container-Dateisystem.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/cp>.

- Kopiere eine Datei oder ein Verzeichnis vom Host in einen Container:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis_auf_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis_in_container</span>

- Kopiere eine Datei oder ein Verzeichnis von einem Container zum Host:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis_in_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis_auf_host</span>

- Kopiere eine Datei oder ein Verzeichnis vom Host in einen Container und folge dabei Symlinks (kopiert die verlinkten Dateien statt der Symlinks):

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/symlink_auf_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis_in_container</span>
