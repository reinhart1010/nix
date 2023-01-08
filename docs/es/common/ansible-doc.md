---
layout: page
title: common/ansible-doc (español)
description: "Muestra información sobre los módulos instalados en las bibliotecas de Ansible."
content_hash: 0c88845341096c5da4d3bf05bc24c69783b3d746
last_modified_at: 2023-01-08
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-doc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-doc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-doc.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-doc

Muestra información sobre los módulos instalados en las bibliotecas de Ansible.
Muestra una concisa lista de complementos y sus breves descripciones.
Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Lista de complementos disponibles acorde a su acción (módulos):

`ansible-doc --list`

- Lista de complementos disponibles dado un tipo específico:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` --list`

- Muestra información sobre un complemento acorde su acción específica (módulo):

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_complemento</span>

- Muestra información acerca de un complemento dado un tipo específico:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_complemento</span>

- Muestra fragmentos de las acciones respecto al tipo de complemento y su especificidad de tipo de acción (módulos):

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_complemento</span>

- Muestra información de acuerdo al complemento dada su especificidad de acción (módulo) como JSON:

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_complemento</span>
