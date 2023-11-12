---
layout: page
title: common/entr (polski)
description: "Uruchom dowolną komendę, gdy zmieni się plik."
content_hash: a38ef0b28679a0ca1887179abbfdfee2688a5560
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/entr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/entr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# entr

Uruchom dowolną komendę, gdy zmieni się plik.
Więcej informacji: <https://manned.org/entr>.

- Przebuduj projekt używając `make`, jeżeli zmiemi się którykolwiek z plików w podkatalogu:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Jeżeli zmieni się którykowliek z plików źródłowych `.c` w obecnym katalogu, przebuduj i uruchom testy używając `make`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- Wyślij `SIGTERM` do wszystkich uruchomionych poprzednio podprocesów ruby przed wykonaniem `ruby main.rb`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- Uruchom komendę przekazując zmieniony plik (`/_`) jako jej argument:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`
