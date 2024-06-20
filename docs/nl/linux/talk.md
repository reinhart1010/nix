---
layout: page
title: linux/talk (Nederlands)
description: "Een visueel communicatieprogramma dat regels van jouw terminal kopieert naar die van een andere gebruiker."
content_hash: 3b6672922143b5e64b74b605099d72ae07be660d
last_modified_at: 2024-06-20
related_topics:
  - title: English version
    url: /en/linux/talk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# talk

Een visueel communicatieprogramma dat regels van jouw terminal kopieert naar die van een andere gebruiker.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/talk-invocation.html>.

- Start een talk-sessie met een gebruiker op dezelfde machine:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Start een talk-sessie met een gebruiker op dezelfde machine, die is ingelogd op tty3:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty3</span>

- Start een talk-sessie met een gebruiker op een externe machine:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Wis tekst op beide terminals:

`<Ctrl>+D`

- Verlaat de talk-sessie:

`<Ctrl>+C`
