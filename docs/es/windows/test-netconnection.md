---
layout: page
title: windows/test-netconnection (español)
description: "Muestra información de diagnóstico de una conexión."
content_hash: 1d8a4520459ab148f3b7be00c117b75511e6377f
last_modified_at: 2024-04-28
related_topics:
  - title: English version
    url: /en/windows/test-netconnection.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Test-NetConnection

Muestra información de diagnóstico de una conexión.
Este comando solo se puede utilizar a través de PowerShell.
Más información: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- Prueba una conexión y muestra resultados detallados:

`Test-NetConnection -InformationLevel Detailed`

- Prueba una conexión a un host remoto con un número de puerto específico:

`Test-NetConnection -ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_del_host</span>` -Port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_puerto</span>
