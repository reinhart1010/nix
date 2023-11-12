---
layout: page
title: common/ansible-playbook (italiano)
description: "Esegui task definiti nel playbook di un computer remoto via SSH."
content_hash: 36d1fe461ae517ad3229b861a3186a8e5c8d2da2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-playbook.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-playbook.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-playbook.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-playbook

Esegui task definiti nel playbook di un computer remoto via SSH.
Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Esegui tasks nel playbook:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Esegui task nel playbook con un inventory personalizzato:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inventory</span>

- Esegui task nel playvook con variabili aggiuntive definite da linea di comando:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabile1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valore1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabile2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valore2</span>` ..."`

- Esegui task nel playbook con variabili aggiuntive definite in un file JSON:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabili.json</span>`"`
