---
layout: page
title: osx/say (polski)
description: "Czyta na głos."
content_hash: d1033c0a8c015a7e479334963c5da3e05e3e0f69
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/say.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/say.html
    icon: bi bi-globe
tldri18n_status: 2
---
# say

Czyta na głos.
Więcej informacji: <https://keith.github.io/xcode-man-pages/say.1.html>.

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
