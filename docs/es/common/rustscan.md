---
layout: page
title: common/rustscan (español)
description: "Escáner de puertos rápido, escrito en Rust integrado con `nmap`."
content_hash: 7348c099f0594dfac635d8ec994b2971e2c3c279
last_modified_at: 2024-01-23
related_topics:
  - title: English version
    url: /en/common/rustscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustscan

Escáner de puertos rápido, escrito en Rust integrado con `nmap`.
Más información: <https://github.com/RustScan/RustScan>.

- Escanea todos los puertos de una o más direcciones delimitadas por comas usando los valores predeterminados:

`rustscan --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombrehost</span>

- Escanea los [t]op 1000 puertos con detección de servicio y versión:

`rustscan --top --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea una lista específica de [p]uertos:

`rustscan --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto1,puerto2,...,puertoN</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea un rango específico de puertos:

`rustscan --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inicio-fin</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Añade argumentos de script a `nmap`:

`rustscan --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>` -- -A -sC`

- Escanea con un tamaño de lote ([b]atch) (por defecto: 4500) y [t]iempo de espera personalizado (por defecto: 1500ms):

`rustscan --batch-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamaño_lote</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea puertos en un orden específico:

`rustscan --scan-order `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial|random</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>

- Escanea en modo "greppable" (solo imprime los puertos y no usa `nmap`):

`rustscan --greppable --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_o_direcciones</span>
