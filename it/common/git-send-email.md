---
layout: page
title: common/git-send-email (italiano)
description: "Invia una raccolta di patch via email."
content_hash: aea6ca68eecdf8ee36e5b4a99de31d3e94b538e0
related_topics:
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-send-email.html
    icon: bi bi-globe
---
# git send-email

Invia una raccolta di patch via email.
Le patch possono essere specificate come file, cartelle, o liste di revisione.
Maggiori informazioni: <https://git-scm.com/docs/git-send-email>.

- Invia l'ultimo commit nel ramo corrente:

`git send-email -1`

- Invia un commit specifico:

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Invia 10 commit nel ramo corrente:

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- Invia un'email con un messaggio introduttivo alla serie di patch:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_commit</span>` --compose`

- Revisiona e modifica il messaggio email per ogni patch da inviare:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_commit</span>` --annotate`
