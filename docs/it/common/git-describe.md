---
layout: page
title: common/git-describe (italiano)
description: "Rendi il nome di un oggetto Git più leggibile usando i riferimenti disponibili."
content_hash: 549a3a9ef18950b74eca25e9307d4a13880944ca
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-describe.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-describe.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-describe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git describe

Rendi il nome di un oggetto Git più leggibile usando i riferimenti disponibili.
Maggiori informazioni: <https://git-scm.com/docs/git-describe>.

- Crea un nome univoco per il commit corrente (il nome contiene i tag più recenti, il numero di commit aggiuntivi, e l'hash breve del commit):

`git describe`

- Crea un nome di 4 cifre per l'hash breve del commit:

`git describe --abbrev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Genera un nome che includa anche il percorso di riferimento:

`git describe --all`

- Descrivi un tag Git:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.0.0</span>

- Crea un nome per l'ultimo commit di un dato ramo:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
