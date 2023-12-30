---
layout: page
title: common/docker-exec (italiano)
description: "Esegui un comando su un Docker container in esecuzione."
content_hash: e813bd291dc22664358390d2100c2c6c841b8d86
last_modified_at: 2023-12-30
related_topics:
  - title: Deutsch version
    url: /de/common/docker-exec.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-exec.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-exec.html
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

Esegui un comando su un Docker container in esecuzione.
Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Avvia una shell interattiva all'interno di un container in esecuzione:

`docker exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Esegui un commando in background ("detached") su un container in esecuzione:

`docker exec --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Seleziona la directory di lavoro in cui eseguire un dato comando:

`docker exec --interactive --tty --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Esegui un comando in background su un container esistente, mantenendo aperto `stdin`:

`docker exec --interactive --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Imposta una variabile d'ambiente in una sessione bash in esecuzione:

`docker exec --interactive --tty --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_variabile</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Specifica l'utente da usare per eseguire un comando:

`docker exec --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
