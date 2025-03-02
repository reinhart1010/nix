---
layout: page
title: common/snmpget (español)
description: "Consulta utilizando el protocolo SNMP."
content_hash: 701251f894e0e1446e083df94ab395a1849cf2d2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/snmpget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snmpget

Consulta utilizando el protocolo SNMP.
Más información: <https://manned.org/snmpget>.

- Solicita un único valor al agente SNMP:

`snmpget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comunidad</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>

- Muestra la ruta completa del identificador de objeto (OID):

`snmpget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comunidad</span>` -O f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>
