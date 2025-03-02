---
layout: page
title: common/dbx (español)
description: "Interactúa con la plataforma Databricks."
content_hash: d4c8648e8387ebfdf2609fad179335baa55c2972
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/dbx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dbx

Interactúa con la plataforma Databricks.
Nota: esta herramienta ha sido retirada y se recomienda utilizar Databricks Asset Bundles en su lugar.
Más información: <https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>.

- Crea un nuevo proyecto `dbx` en el directorio de trabajo actual:

`dbx configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DEFAULT</span>

- Sincroniza archivos locales de la ruta especificada a DBFS y vigila los cambios:

`dbx sync dbfs --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>` --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_remoto</span>

- Despliega el flujo de trabajo especificado en el almacenamiento de artefactos:

`dbx deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_flujo_de_trabajo</span>

- Inicia el flujo de trabajo especificado después de desplegarlo:

`dbx launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_flujo_de_trabajo</span>
