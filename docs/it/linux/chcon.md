---
layout: page
title: linux/chcon (italiano)
description: "Cambia contesto di sicurezza SELinux di file o directory."
content_hash: 2c1e73c21eb7e18a4ee2ddafa383ab71fe1f120c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/chcon.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/chcon.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/chcon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/chcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcon

Cambia contesto di sicurezza SELinux di file o directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- Mostra il contesto di sicurezza di un file:

`ls -lZ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Cambia il contesto di sicurezza di un file usandone un'altro come riferimento:

`chcon --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_riferimento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Cambia l'intero contesto di sicurezza SELinux di un file:

`chcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruolo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range/livello</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Cambia solo l'utente di un contesto di sicurezza SELinux:

`chcon -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Cambia solo il ruolo di un contesto di sicurezza SELinux:

`chcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruolo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Cambia solo il tipo di un contesto di sicurezza SELinux:

`chcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Cambia solo il range/livello di un contesto di sicurezza SELinux:

`chcon -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range/livello</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
