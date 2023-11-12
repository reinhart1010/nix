---
layout: page
title: common/docker-exec (Deutsch)
description: "Führe Befehle in einem bereits laufenden Docker Container aus."
content_hash: b306eb1fc85de5f294c1be3c5906bbaae0698b7c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-exec.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-exec.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-exec.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-exec.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker exec

Führe Befehle in einem bereits laufenden Docker Container aus.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Öffne eine Shell innerhalb eines bereits laufenden Containers:

`docker exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Führe einen Befehl im Hintergrund (losgelöst) in einem laufenden Container aus:

`docker exec --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Bestimme das Arbeitsverzeichnis, in dem der Befehl ausgeführt werden soll:

`docker exec --interactive -tty --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Führe einen Befehl im Hintergrund in einem laufenden Container aus, aber lies von der Standardeingabe:

`docker exec --interactive --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Setze eine Umgebungsvariable in einer laufenden Bash Sitzung:

`docker exec --interactive --tty --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variablen_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Führe einen Befehl als ein bestimmter Benutzer aus:

`docker exec --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>
