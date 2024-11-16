---
layout: page
title: common/gitleaks (español)
description: "Detecta secretos y claves API filtradas en repositorios Git."
content_hash: a1030f45f472c322efe2ce0a66c739d32d6159f7
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/gitleaks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gitleaks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitleaks

Detecta secretos y claves API filtradas en repositorios Git.
Más información: <https://github.com/gitleaks/gitleaks>.

- Escanea un repositorio remoto:

`gitleaks detect --repo-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/usuario/repositorio.git</span>

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
