---
layout: page
title: common/dexter (italiano)
description: "Strumento per autenticare utenti kubectl con OpenId Connect."
content_hash: d9bc9fcf82b0bb07404c13d65154135edbe54cf0
related_topics:
  - title: English version
    url: /en/common/dexter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dexter.html
    icon: bi bi-globe
---
# dexter

Strumento per autenticare utenti kubectl con OpenId Connect.
Maggiori informazioni: <https://github.com/gini/dexter>.

- Crea ed autentica un utente con Google OIDC:

`dexter auth -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id-client</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segreto-client</span>

- Sovrascrivi la posizione predefinita della configurazione di kube:

`dexter auth -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id-client</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segreto-client</span>` --kube-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/config</span>
