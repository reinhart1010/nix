---
layout: page
title: common/kopia (español)
description: "Herramienta de copia de seguridad de código abierto, rápida y segura."
content_hash: 686aef1215facb91dc48b8970127061edd0a1dc7
last_modified_at: 2024-01-26
related_topics:
  - title: English version
    url: /en/common/kopia.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kopia.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kopia

Herramienta de copia de seguridad de código abierto, rápida y segura.
Soporta encriptación, compresión, deduplicación e instantáneas incrementales.
Más información: <https://kopia.io/docs/reference/command-line/>.

- Crea un repositorio en el sistema de archivos local:

`kopia repository create filesystem --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio_local</span>

- Crea un repositorio en Amazon S3:

`kopia repository create s3 --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_bucket</span>` --access-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_clave_de_acceso_AWS</span>` --secret-access-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_de_acceso_secreta_AWS</span>

- Conecta a un repositorio:

`kopia repository connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_de_repositorio</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio</span>

- Crea una instantánea de un directorio:

`kopia snapshot create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista instantáneas:

`kopia snapshot list`

- Restaura una instantánea en un directorio específico:

`kopia snapshot restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_instantánea</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_objetivo</span>

- Crea una nueva política:

`kopia policy set --global --keep-latest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_instantáneas_a_mantener</span>` --compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algoritmo_de_compresión</span>

- Excluye un archivo o directorio específico de las copias de seguridad:

`kopia policy set --global --add-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>
