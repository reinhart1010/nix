---
layout: page
title: common/trufflehog (español)
description: "Encuentra y verifica credenciales en archivos, repositorios de Git, cubos S3 e imágenes Docker."
content_hash: d683fe0083535175e56f4fcd419775149a292394
last_modified_at: 2024-03-02
related_topics:
  - title: English version
    url: /en/common/trufflehog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/trufflehog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trufflehog

Encuentra y verifica credenciales en archivos, repositorios de Git, cubos S3 e imágenes Docker.
Más información: <https://github.com/trufflesecurity/trufflehog>.

- Escanea un repositorio de Git en busca de secretos verificados:

`trufflehog git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --only-verified`

- Escanea una organización de GitHub en busca de secretos verificados:

`trufflehog github --org=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trufflesecurity</span>` --only-verified`

- Escanea un repositorio de GitHub en busca de claves verificadas y genera un archivo de salida JSON:

`trufflehog git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --only-verified --json`

- Escanea un repositorio de GitHub junto con sus incidencias y solicitudes de extracción:

`trufflehog github --repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --issue-comments --pr-comments`

- Escanea un cubo S3 en busca de claves verificadas:

`trufflehog s3 --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_cubo</span>` --only-verified`

- Escanea cubos S3 utilizando roles IAM:

`trufflehog s3 --role-arn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iam-role-arn</span>

- Escanea archivos o directorios individuales:

`trufflehog filesystem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>

- Escanea una imagen de Docker en busca de secretos verificados:

`trufflehog docker --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trufflesecurity/secrets</span>` --only-verified`
