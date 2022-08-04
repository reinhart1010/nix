---
layout: page
title: common/vim (polski)
description: "Vim (Vi IMproved), edytor tekstu wiersza polecenia, oferuje kilka trybów dla różnych rodzajów manipulacji tekstem."
content_hash: a7be85009f6c0008a33246266ff13eae29883888
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---
# vim

Vim (Vi IMproved), edytor tekstu wiersza polecenia, oferuje kilka trybów dla różnych rodzajów manipulacji tekstem.
Naciśnięcie przycisku `i` powoduje przejście do trybu edycji. `<Esc>` wraca do normalnego trybu, który nie pozwala na zwykłe wstawianie tekstu.
Więcej informacji: <https://www.vim.org>.

- Otwórz plik:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik</span>

- Otwórz plik pod określonym numerem wiersza:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numer_linii</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik</span>

- Zobacz instrukcję pomocy Vim:

`:help<Enter>`

- Zapisz plik:

`:write<Enter>`

- Wyjdź bez zapisywania:

`:quit!<Enter>`

- Cofnij ostatnią operację:

`u`

- Wyszukaj wzorzec w pliku (naciśnij `n`/`N` przejść do następnego/poprzedniego dopasowania):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">szukaj_wzorca</span>`<Enter>`

- Wykonaj podstawienie wyrażenia regularnego w całym pliku:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zastąpienie</span>`/g<Enter>`
