---
layout: page
title: linux/nsenter (español)
description: "Ejecuta un nuevo comando en el espacio de nombres de un proceso en ejecución."
content_hash: 6c42fa526d81cadc12828abf985b3c4ac4a5d785
last_modified_at: 2024-08-05
related_topics:
  - title: English version
    url: /en/linux/nsenter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nsenter

Ejecuta un nuevo comando en el espacio de nombres de un proceso en ejecución.
Particularmente útil para imágenes Docker o jaulas chroot.
Más información: <https://manned.org/nsenter>.

- Ejecuta un comando específico utilizando los mismos espacios de nombres como un proceso existente:

`nsenter --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_del_comando</span>

- Ejecuta un comando específico en el espacio de nombres mount|UTS|IPC|network|PID|user|cgroup|time de un proceso existente:

`nsenter --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mount|uts|ipc|net|pid|user|cgroup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_del_comando</span>

- Ejecuta un comando específico en los espacios de nombres UTS, time e IPC de un proceso existente:

`nsenter --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --uts --time --ipc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_del_comando</span>

- Ejecuta un comando específico en el espacio de nombres de un proceso existente haciendo referencia a procfs:

`nsenter --pid=/proc/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>`/pid/net -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_del_comando</span>
