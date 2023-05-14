---
layout: page
title: linux/loginctl (polski)
description: "Zarządzaj menedżerem logowania systemd."
content_hash: 507226cbff303593d0a9169583e946f098b65258
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/loginctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># loginctl

Zarządzaj menedżerem logowania systemd.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/loginctl.html>.

- Wyświetl wszystkie aktualne sesje:

`loginctl list-sessions`

- Wyświetl wszystkie właściwości podanej sesji:

`loginctl show-session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_sesji</span>` --all`

- Wyświetl wszystkie właściwości podanego użytkownika:

`loginctl show-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>

- Wyświetl podaną właściwość użytkownika:

`loginctl show-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --property=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_właściwości</span>

- Uruchom operację `loginctl` na zdalnym hoście:

`loginctl list-users -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_hosta</span>
