---
layout: page
title: linux/fpsync (español)
description: "Ejecuta varios procesos de sincronización localmente o en varios trabajadores remotos a través de SSH."
content_hash: 192a402e8014d9b19995d6fd7eec55bb78720b92
last_modified_at: 2024-07-01
related_topics:
  - title: English version
    url: /en/linux/fpsync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fpsync

Ejecuta varios procesos de sincronización localmente o en varios trabajadores remotos a través de SSH.
Más información: <https://www.fpart.org/fpsync/>.

- Sincroniza recursivamente un directorio a otra ubicación:

`fpsync -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/origen/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/destino/</span>

- Sincroniza recursivamente un directorio con la última pasada (activa la opción `--delete` de rsync con cada trabajo de sincronización):

`fpsync -v -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/origen/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/destino/</span>

- Sincroniza recursivamente un directorio a un destino utilizando 8 trabajos de sincronización simultáneos:

`fpsync -v -n 8 -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/origen/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/destino/</span>

- Sincroniza recursivamente un directorio a un destino utilizando 8 trabajos de sincronización concurrentes repartidos entre dos trabajadores remotos (máquina1 y máquina2):

`fpsync -v -n 8 -E -w login@machine1 -w login@machine2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/directorio/compartido</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/origen/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/destino/</span>

- Sincroniza recursivamente un directorio a un destino utilizando cuatro trabajadores locales, cada uno transfiriendo como máximo 1000 archivos y 100 MB por trabajo de sincronización:

`fpsync -v -n 4 -f 1000 -s $((100 * 1024 * 1024)) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/origen/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/destino/</span>

- Sincroniza de forma recursiva cualquier directorio pero excluye archivos `.snapshot*` específicos (Nota: las opciones y los valores deben estar separados por un carácter de tubería):

`fpsync -v -O "-x|.snapshot*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/origen/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/destino/</span>
