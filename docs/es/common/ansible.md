---
layout: page
title: common/ansible (español)
description: "Gestiona grupos de ordenadores de forma remota a través de SSH. (usa el fichero `/etc/ansible/hosts` para añadir nuevos grupos de hosts)."
content_hash: 8555242eb6029b7bc52984e162dbdeebe1b33ef9
last_modified_at: 2024-05-22
related_topics:
  - title: Deutsch version
    url: /de/common/ansible.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ansible.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible

Gestiona grupos de ordenadores de forma remota a través de SSH. (usa el fichero `/etc/ansible/hosts` para añadir nuevos grupos de hosts).
Algunos subcomandos como `ansible galaxy` tienen su propia documentación.
Más información: <https://www.ansible.com/>.

- Lista los hosts pertenecientes a un grupo:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` --list-hosts`

- Hace ping a un grupo de hosts invocando al módulo ping:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -m ping`

- Muestra información sobre un grupo de hosts invocando al módulo setup:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -m setup`

- Ejecuta un comando en un grupo de hosts invocando el módulo de command con argumentos:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mi_comando</span>`'`

- Ejecuta un comando con privilegios administrativos:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mi_comando</span>`'`

- Ejecuta un comando utilizando un archivo de inventario personalizado:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_inventario</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mi_comando</span>`'`

- Lista los grupos de un inventario:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
