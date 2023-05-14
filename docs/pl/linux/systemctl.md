---
layout: page
title: linux/systemctl (polski)
description: "Kontroluj systemd i menedżera usług."
content_hash: c0a58bb36b8c83d75b78d337a12cc48fdc146b40
last_modified_at: 2023-05-14
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemctl

Kontroluj systemd i menedżera usług.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Wyświetl wszystkie działające usługi:

`systemctl status`

- Wyświetl nieudane jednostki:

`systemctl --failed`

- Uruchom/Zatrzymaj/Zrestartuj/Przeładuj usługę:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>

- Wyświetl status jednostki:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>

- Włącz/Wyłącz automatyczne uruchamianie jednostki przy starcie systemu:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>

- Zamaskuj/Zdemaskuj jednostkę, aby uniemożliwić włączanie i ręczną aktywację:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>

- Przeładuj systemd, skanując w poszukiwaniu nowych lub zmienionych jednostek:

`systemctl daemon-reload`

- Sprawdź, czy jednostka jest włączona:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>
