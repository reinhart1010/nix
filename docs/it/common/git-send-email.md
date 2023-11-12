---
layout: page
title: common/git-send-email (italiano)
description: "Invia una raccolta di patch via email."
content_hash: c269703ab27e3d14cfc595cf994df4c567ca7f19
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-send-email.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-send-email.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git send-email

Invia una raccolta di patch via email.
Le patch possono essere specificate come file, directory, o liste di revisione.
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
