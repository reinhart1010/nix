---
layout: page
title: linux/journalctl (polski)
description: "Przeszukaj dziennik systemd."
content_hash: 2b8973cf02655791c4eee2fb6bae75364c69e17b
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/journalctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/journalctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# journalctl

Przeszukaj dziennik systemd.
Więcej informacji: <https://manned.org/journalctl>.

- Wyświetl wszystkie wiadomości o priorytecie 3 (błędy) z tego rozruchu:

`journalctl -b --priority=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Usuń dzienniki starsze niż 2 dni:

`journalctl --vacuum-time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2d</span>

- Wyświetlaj nowe wiadomości (jak `tail -f` dla tradycyjnego sysloga):

`journalctl -f`

- Wyświetl wszystkie wiadomości podanej jednostki:

`journalctl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>

- Wyświetl wiadomości podanej jednostki od czasu jej ostatniego uruchomienia:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jednostka</span>`)`

- Filtruj wiadomości w zakresie czasu (znacznik czasu lub symbol zastępczy, np. "yesterday"):

`journalctl --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">now|today|yesterday|tomorrow</span>` --until "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD HH:MM:SS</span>`"`

- Wyświetl wszystkie wiadomości podanego procesu:

`journalctl _PID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Wyświetl wszystkie wiadomości podanego pliku wykonywalnego:

`journalctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>
