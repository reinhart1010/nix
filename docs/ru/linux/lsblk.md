---
layout: page
title: linux/lsblk (русский)
description: "Отобразить информацию об устройствах."
content_hash: 9793a893673be3f853fb93c12da5cb8e11083f78
last_modified_at: 2025-03-02
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

- Отобразить список всех накопителей в древовидном виде:

`lsblk`

- Отобразить все устройства, в том числе "пустые":

`lsblk -a`

- Отобразить столбец SIZE в байтах, а не в удобочитаемом формате:

`lsblk -b`

- Вывод информации о файловой системе:

`lsblk -f`

- Использовать символы ASCII при отображении в формате дерева:

`lsblk -i`

- Вывести информацию о топологии блочного устройства:

`lsblk -t`

- Исключить устройства, указанные в списке основных номеров устройств, разделенных запятыми:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7,...</span>

- Отобразить вывод с указанием списка определённых параметров, разделенных запятыми:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...</span>
