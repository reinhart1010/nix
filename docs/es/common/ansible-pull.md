---
layout: page
title: common/ansible-pull (español)
description: "Extrae playbooks ansible de un repositorio VCS y los ejecuta para el host local."
content_hash: f72dc3231f20b425c2610e5e13398c8a6699145b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-pull

Extrae playbooks ansible de un repositorio VCS y los ejecuta para el host local.
Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Extrae un playbook de un VCS y ejecuta local.yml del playbook por defecto:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositorio</span>

- Extrae un playbook de un VCS y ejecuta un playbook específico:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Extrae un playbook de un VCS en una rama determinada y ejecuta un playbook específico:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositorio</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Extrae un playbook de un VCS, en tanto especificando un archivo hosts y ejecuta un playbook específico:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositorio</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_hosts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>
