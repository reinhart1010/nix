---
layout: page
title: common/uv-add (español)
description: "Añade dependencias de paquetes al archivo `pyproject.toml`."
content_hash: d3a9bcfcbd30546cf4c57746b71e2853c4fe4a14
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/uv-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv add

Añade dependencias de paquetes al archivo `pyproject.toml`.
Los paquetes se especifican según <https://peps.python.org/pep-0508/>.
Más información: <https://docs.astral.sh/uv/reference/cli/#uv-add>.

- Añade la última versión de un paquete:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Añade múltiples paquetes:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Añade un paquete con un requisito de versión:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete>=1.2.3</span>

- Añade paquetes a un grupo de dependencia opcional, que se incluirá cuando se publique:

`uv add --optional `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opcional</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Añade paquetes a un grupo local, que no se incluirán cuando se publiquen:

`uv add --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Añade paquetes al grupo dev, abreviatura de `--group dev`:

`uv add --dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Añade paquete como editable:

`uv add --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/paquete/</span>

- Habilita un extra al instalar el paquete, se puede proporcionar varias veces:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">característica_extra</span>
