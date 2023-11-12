---
layout: page
title: common/docker-cp (italiano)
description: "Copia file o directory tra il filesystem di un container e quello locale (host)."
content_hash: 70af51da6aff6b1418d44800645f19720598aff2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-cp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker cp

Copia file o directory tra il filesystem di un container e quello locale (host).
Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/cp>.

- Copia un file o una directory dall'host a un container:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_su_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_su_container</span>

- Copia un file o una directory da un container all'host:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_su_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_su_host</span>

- Copia un file o una directory dall'host a un container, seguendo un link simbolico (non copiare il link simbolico, ma direttamente il file da lui referenziato):

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/link_simbolico_su_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_su_container</span>
