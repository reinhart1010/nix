---
layout: page
title: common/cppcheck (italiano)
description: "Strumento di analisi statica per codice C/C++."
content_hash: 12952e97036746d180313337ea7f9467a20b8c11
related_topics:
  - title: English version
    url: /en/common/cppcheck.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cppcheck.html
    icon: bi bi-globe
---
# cppcheck

Strumento di analisi statica per codice C/C++.
Piuttosto che sugli errori di sintassi, si concentra su tipi di bug che normalmente non vengono rilevati dai compilatori.
Maggiori informazioni: <http://cppcheck.sourceforge.net>.

- Controlla la directory corrente ricorsivamente, mostrando il progresso a schermo e loggando i messaggi di errore in un file:

`cppcheck . 2> cppcheck.log`

- Controlla una determinata directory ricorsivamente, senza stampare informazioni sul progresso:

`cppcheck --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Controlla un determinato file, specificando quali test eseguire (di default, solo gli errori sono mostrati):

`cppcheck --enable=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warning|style|performance|portability|information|all</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.cpp</span>

- Elenca i test disponibili:

`cppcheck --errorlist`

- Controlla un determinato file, ignorando specifici test:

`cppcheck --suppress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_test1</span>` --suppress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">it_test2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.cpp</span>

- Controlla la directory corrente, fornendo percorsi da includere per file esterni (e.g. librerie esterne):

`cppcheck -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">include/directory_1</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">include/directory_2</span>` .`

- Controlla un progetto Microsoft Visual Studio (`*.vcxproj`) o file solution (`*.sln`):

`cppcheck --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/progetto.sln</span>
