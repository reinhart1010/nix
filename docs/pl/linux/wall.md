---
layout: page
title: linux/wall (polski)
description: "Pisze wiadomość na terminalach aktualnie zalogowanych użytkowników."
content_hash: d508bf35ef1cd665a3099d1c1d0009b3343b3b67
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/wall.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wall

Pisze wiadomość na terminalach aktualnie zalogowanych użytkowników.
Więcej informacji: <https://manned.org/wall>.

- Wysłanie wiadomości:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiadomość</span>`" | wall`

- Wysłanie wiadomoci z pliku:

`wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Wysłanie wiadomość z pliku z podanym timeoutem (sekundy, domyślnie 300):

`wall -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekundy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>
