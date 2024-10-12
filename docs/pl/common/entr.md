---
layout: page
title: common/entr (polski)
description: "Uruchom dowolną komendę, gdy zmieni się plik."
content_hash: aa0ca9df2c293cda1cf3d436795161f51ef6a626
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/entr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/entr.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># entr

Uruchom dowolną komendę, gdy zmieni się plik.
Więcej informacji: <https://eradman.com/entrproject/>.

- Przebuduj projekt używając `make`, jeżeli zmiemi się którykolwiek z plików w podkatalogu:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Jeżeli zmieni się którykowliek z plików źródłowych `.c` w obecnym katalogu, przebuduj i uruchom testy używając `make`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- Wyślij `SIGTERM` do wszystkich uruchomionych poprzednio podprocesów ruby przed wykonaniem `ruby main.rb`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- Uruchom komendę przekazując zmieniony plik (`/_`) jako jej argument:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`
