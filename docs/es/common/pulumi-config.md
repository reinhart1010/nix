---
layout: page
title: common/pulumi-config (español)
description: "Administra la configuración de una pila Pulumi."
content_hash: 857d234dcd6cd8c7d406c4db3d54eaa305e042c0
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/common/pulumi-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi config

Administra la configuración de una pila Pulumi.
Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- Muestra la configuración actual en formato JSON:

`pulumi config --json`

- Obtiene el valor de una clave de configuración:

`pulumi config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>

- Elimina un valor de configuración:

`pulumi config rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>

- Establece un valor para una clave de configuración desde un archivo:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` | pulumi config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>

- Establece un valor secreto (por ejemplo, la clave API) para una clave de configuración y almacena/muestra como texto cifrado:

`pulumi config set --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_53cr3t0</span>

- Elimina varios valores de configuración de un archivo de configuración especificado:

`pulumi config --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` rm-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave1 clave2 ...</span>
