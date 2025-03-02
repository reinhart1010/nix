---
layout: page
title: common/pulumi-env (español)
description: "Administra entornos Pulumi."
content_hash: 1a84778ba0953b6ba762038d7488522096bdf949
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pulumi-env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi env

Administra entornos Pulumi.
Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

- Lista todos los entornos:

`pulumi env ls`

- Crea un entorno:

`pulumi env init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>

- Establece un valor en un entorno:

`pulumi env set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Edita la definición de un entorno:

`pulumi env edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>

- Elimina un valor de un entorno:

`pulumi env rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>

- Elimina un entorno por completo:

`pulumi env rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>

- Muestra la ayuda:

`pulumi env --help`
