---
layout: page
title: common/drill (italiano)
description: "Esegui varie query DNS."
content_hash: 86ca4b8f262515724ca8c9edac6c44dc2230ca70
related_topics:
  - title: English version
    url: /en/common/drill.html
    icon: bi bi-globe
---
# drill

Esegui varie query DNS.
Maggiori informazioni: <https://manned.org/drill>.

- Mostra gli IP associati ad un hostname (record A):

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Lookup the mail server(s) associated with a given domain name (MX record):

`drill mx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Recupera tutti i tipi di record per un dato dominio:

`drill any `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Specifica un server DNS alternativo da interrogare:

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Esegui un lookup DNS inverso su di un indirizzo IP (record PTR):

`drill -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Esegui un tracciamento DNSSEC dai root server fino al dominio:

`drill -TD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Mostra record DNSKEY per un dominio:

`drill -s dnskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>
