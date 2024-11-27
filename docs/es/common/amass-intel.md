---
layout: page
title: common/amass-intel (español)
description: "Recopila información de código abierto sobre una organización, como dominios raíz y ASNs."
content_hash: 74e14614795460b031c204821a0a264e12a67f23
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/amass-intel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-intel.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/amass-intel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/amass-intel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-intel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass intel

Recopila información de código abierto sobre una organización, como dominios raíz y ASNs.
Más información: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Encuentra dominios raíz en un rango de direcciones IP específico:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Usa métodos activos de reconocimiento:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Encuentra dominios raíz relacionados con un [d]ominio específico:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>

- Encuentra ASNs pertenecientes a una [org]anización específica:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_organización</span>

- Encuentra dominios raíz pertenecientes a un Número de Sistema Autónomo específico:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>

- Guarda los resultados en un archivo de texto:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>

- Lista todas las fuentes de datos disponibles:

`amass intel -list`
