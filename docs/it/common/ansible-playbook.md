---
layout: page
title: common/ansible-playbook (italiano)
description: "Esegui task definiti nel playbook di un computer remoto via SSH."
content_hash: 36d1fe461ae517ad3229b861a3186a8e5c8d2da2
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-playbook.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-playbook.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ansible-playbook.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
