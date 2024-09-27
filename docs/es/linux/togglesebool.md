---
layout: page
title: linux/togglesebool (español)
description: "Voltea los valores actuales (no persistentes) de los booleanos de SELinux."
content_hash: 8d7fd82a09803cb7768965ed086a19fe32d68798
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/togglesebool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/togglesebool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># togglesebool

Voltea los valores actuales (no persistentes) de los booleanos de SELinux.
Nota: Esta herramienta ha quedado obsoleta y a menudo se elimina en favor de `setsebool`.
Más información: <https://manned.org/togglesebool>.

- Cambia los valores actuales (no persistentes) de los booleanos especificados:

`sudo togglesebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virt_use_samba virt_use_usb ...</span>
