---
layout: page
title: osx/say (polski)
description: "Czyta na głos."
content_hash: f06641112cc00f936522f5b2fd37ed75ca63db35
last_modified_at: 2022-11-22
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/say.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># say

Czyta na głos.
Więcej informacji: <https://ss64.com/osx/say.html>.

- Powiedz na głos:

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lubię jeździć na rowerze.</span>`"`

- Przeczytaj z pliku:

`say --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.txt</span>

- Przeczytaj używając konkretnego głosu i prędkości mowy:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">głos</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">słowa_na_minutę</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Przepraszam Dave, ale nie mogę Ci na to pozwolić.</span>`"`

- Pokaż listę dostępnych głosów, różne głosy obsługują różne języki:

`say --voice="?"`

- Powiedz coś po angielsku:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Alex</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Here's to the Crazy Ones.</span>`"`

- Stwórz plik audio z tekstu:

`say --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Litwo, ojczyzno moja!</span>`"`
