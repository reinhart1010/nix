---
layout: page
title: linux/systemctl (українська)
description: "Керуйте системою systemd і диспетчером служб."
content_hash: 6ce2917cb10ebd081d2a7dd9f97423fc645bd885
last_modified_at: 2023-11-12
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
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

Керуйте системою systemd і диспетчером служб.
Більше інформації: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Відобразити всі запущені служби:

`systemctl status`

- Відобразити список служб, які не запустилися через помилки:

`systemctl --failed`

- Запуск/зупинка/перезапуск/перезавантаження служби:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">служба</span>

- Показати статус служби:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">служба</span>

- Увімкнути/вимкнути запуск служби під час завантаження:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">служба</span>

- Маскування/розкриття служби, щоб запобігти ввімкненню та ручній активації:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">служба</span>

- Перезавантажити systemd, шукати нові або змінені пристрої:

`systemctl daemon-reload`

- Перевірити, чи ввімкнено службу до автозавантаження:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">служба</span>
