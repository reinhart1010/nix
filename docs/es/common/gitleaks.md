---
layout: page
title: common/gitleaks (español)
description: "Detecta secretos y claves API filtradas en repositorios Git."
content_hash: c13aca76401fb5330a3fadfe261fc7a20d5201a7
last_modified_at: 2024-05-03
related_topics:
  - title: English version
    url: /en/common/gitleaks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitleaks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitleaks

Detecta secretos y claves API filtradas en repositorios Git.
Más información: <https://github.com/gitleaks/gitleaks>.

- Escanea un repositorio remoto:

`gitleaks detect --repo-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/nombre_usuario/repositorio.git</span>

- Escanea un directorio local:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio</span>

- Crea un archivo JSON con los resultados del análisis:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio</span>` --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/informe.json</span>

- Utiliza un archivo de reglas personalizado:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio</span>` --config-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_configuración.toml</span>

- Inicia la búsqueda a partir de una confirmación específica:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio</span>` --log-opts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--since=identificador_confirmación</span>

- Escanea cambios no confirmados antes de una confirmación:

`gitleaks protect --staged`

- Muestra información detallada que indica que partes se identificaron como fugas durante el análisis:

`gitleaks protect --staged --verbose`
