---
layout: page
title: linux/lsblk (русский)
description: "Отобразить информацию об устройствах."
content_hash: c8dd3cc2136117aeb4538f261e4a6ea70788c737
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsblk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/lsblk.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/lsblk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsblk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsblk

Отобразить информацию об устройствах.
Больше информации: <https://manned.org/lsblk>.

- Отобразить список всех накопителей в древовидноv виде:

`lsblk`

- Отобразить все устройства, в том числе "пустые":

`lsblk -a`

- Отобразить столбец SIZE в байтах, а не в удобночитаемом формате:

`lsblk -b`

- Вывод информации о файловой системе:

`lsblk -f`

- Использовать символы ASCII при отображении в формате дерева:

`lsblk -i`

- Вывести информацию о топологии блочного устройства:

`lsblk -t`

- Исключить устройства, указанные в списке основных номеров устройств, разделенных запятыми:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7</span>

- Отобразить вывод с указанием списка определённых параметров, разделенных запятыми:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SERIAL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MODEL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TRAN</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIZE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FSTYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MOUNTPOINT</span>
