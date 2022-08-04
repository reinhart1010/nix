---
layout: page
title: common/bosh (italiano)
description: "Strumento da linea di comando per distribuire e gestire director BOSH."
content_hash: 48c9792129a3fe265b6b4277c2694601c8d1cc9f
related_topics:
  - title: English version
    url: /en/common/bosh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bosh.html
    icon: bi bi-globe
---
# bosh

Strumento da linea di comando per distribuire e gestire director BOSH.
Maggiori informazioni: <https://bosh.io/docs/cli-v2/>.

- Crea un alias locale per un director:

`bosh alias-env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_ip|url</span>` --ca-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificato_ca</span>

- Elenca ambienti:

`bosh environments`

- Esegui il login al director:

`bosh login -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>` `

- Elenca deployment (distribuzioni):

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>` deployments`

- Elenca le macchine virtuali in un ambiente:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>` vms -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment</span>

- Avvia una sessione SSH in una macchina virtuale:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macchina_virtuale</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment</span>

- Carica una stemcell:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>` upload-stemcell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_stemcell|url</span>

- Mostra la configurazione cloud attuale:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ambiente</span>` cloud-config`
