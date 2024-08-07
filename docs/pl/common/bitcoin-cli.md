---
layout: page
title: common/bitcoin-cli (polski)
description: "Klient konsolowy do interakcji z demonem Bitcoina poprzez zapytania RPC."
content_hash: fe93e2ee62e796d0e459d3812db61a25551d9b17
last_modified_at: 2024-07-26
related_topics:
  - title: English version
    url: /en/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bitcoin-cli.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bitcoin-cli

Klient konsolowy do interakcji z demonem Bitcoina poprzez zapytania RPC.
Używa konfiguracji zdefiniowanej w `bitcoin.conf`.
Więcej informacji: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Wyślij transakcję na dany adres:

`bitcoin-cli sendtoaddress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ilość</span>

- Wygeneruj jeden lub więcej bloków:

`bitcoin-cli generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ilość_bloków</span>

- Wyświetl informacje o portfelu:

`bitcoin-cli getwalletinfo`

- Wyświetl wszystkie poprzednie transakcje dostępne do opłacenia transakcji wychodzących:

`bitcoin-cli listunspent`

- Wyeksportuj dane portfela do pliku tekstowego:

`bitcoin-cli dumpwallet "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>`"`
