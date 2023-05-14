---
layout: page
title: linux/systemd-run (polski)
description: "Uruchamiaj programy w przejściowych jednostkach zakresu, jednostkach usługowych lub jednostkach usługowych uruchamianych przez ścieżkę, gniazdo lub timer."
content_hash: d01f2840aa15a3dec0ad65c3e04db4be0c112e3e
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/systemd-run.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-run

Uruchamiaj programy w przejściowych jednostkach zakresu, jednostkach usługowych lub jednostkach usługowych uruchamianych przez ścieżkę, gniazdo lub timer.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- Uruchom przejściową usługę:

`sudo systemd-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Uruchom przejściową usługę pod menedżerem usług aktualnego użytkownika (bez uprawnień):

`systemd-run --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Uruchom przejściową usługę z podaną nazwą jednostki i opisem:

`sudo systemd-run --unit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>` --description=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Uruchom przejściową usługę, która nie jest czyszczona po jej zakończeniu z podaną zmienną środowiskową:

`sudo systemd-run --remain-after-exit --set-env=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartość</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Uruchom przejściowy timer, który okresowo uruchamia swoją przejściową usługę (zobacz `man systemd.time`, aby zapoznać się z formatem wydarzeń kalendarza):

`sudo systemd-run --on-calendar=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wydarzenie_kalendarza</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Udostępnij terminal programowi (umożliwiając interaktywne wejście/wyjście) i zapewnij, że szczegóły wykonania pozostaną po zakończeniu programu:

`systemd-run --remain-after-exit --pty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>

- Ustaw właściwości (np. CPUQuota, MemoryMax) procesu i poczekaj, aż się zakończy:

`systemd-run --property MemoryMax=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pamięć_w_bajtach</span>` --property CPUQuota=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">procent_czasu_CPU</span>`% --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>

- Użyj programu w potoku powłoki:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda1</span>` | systemd-run --pipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda3</span>
