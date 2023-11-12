---
layout: page
title: windows/choco-pin (polski)
description: "Przypięcie obecnej bądź podanej wersji dla danego pakietu zarządzanego przez Chocolatey."
content_hash: 2597ad20b264ea942ad7dd35fffca9682bc11b10
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pin.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pin.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pin.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco pin

Przypięcie obecnej bądź podanej wersji dla danego pakietu zarządzanego przez Chocolatey.
Przypięte pakiety są automatycznie pomijane podczas aktualizacji pakietów.
Więcej informacji: <https://chocolatey.org/docs/commands-pin>.

- Wyświetlanie listy obecnie przypiętych pakietów wraz z wersjami:

`choco pin list`

- Przypnij pakiet w jego obecnej wersji:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Przypnij pakiet w podanej wersji:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wersja</span>

- Odepnij dany pakiet:

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>
