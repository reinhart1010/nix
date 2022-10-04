---
layout: page
title: windows/msg (polski)
description: "Wyślij wiadomość do wybranego użytnownika lub sesji:"
content_hash: b9215afeeb46c41a8c13c10d086f63544d420fa5
related_topics:
  - title: English version
    url: /en/windows/msg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/msg.html
    icon: bi bi-globe
---
# msg

Wyślij wiadomość do wybranego użytnownika lub sesji:
Więcej informacji: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- Wysyła wiadomość do użytkownika lub sesji:

`msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika|nazwa_sesji|identyfikator_sesji</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiadomość</span>

- Wyślij wiadomość ze standardowego wejścia

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiadomość</span>`" | msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika|nazwa_sesji|identyfikator_sesji</span>

- Wyślij wiadomość to zdalnej maszyny:

`msg /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_serwera</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika|nazwa_sesji|identyfikator_sesji</span>

- Wyślij wiadomość do wszystkich użytkowników aktualnej maszyny:

`msg *`

- Wyślij wiadomość z opóźnieniem:

`msg /time:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>
