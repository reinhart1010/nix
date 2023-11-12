---
layout: page
title: common/aws-configure (español)
description: "Gestiona la configuración para la CLI de AWS."
content_hash: 84a56f8c508785c03f6bfd102a8f842f469dbd4c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-configure.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws-configure.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-configure.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws configure

Gestiona la configuración para la CLI de AWS.
Más información: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configura AWS CLI interactivamente (crea una nueva configuración o actualiza la predeterminada):

`aws configure`

- Configura un perfil con nombre para la CLI de AWS de forma interactiva (crea un perfil nuevo o actualiza uno existente):

`aws configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>

- Muestra el valor de una variable de configuración específica:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Muestra el valor de una variable de configuración en un perfil específico:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>

- Establece el valor de una variable de configuración específica:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Establece el valor de una variable de configuración en un perfil específico:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>

- Lista las entradas de configuración:

`aws configure list`

- Lista las entradas de configuración para un perfil específico:

`aws configure list --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>
