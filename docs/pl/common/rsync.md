---
layout: page
title: common/rsync (polski)
description: "Przesyłaj pliki do lub ze zdalnego hosta (ale nie pomiędzy dwoma zdalnymi hostami), domyślnie używając SSH."
content_hash: db171d6c631a616b477fe830aa23b99bf948c0e1
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/common/rsync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rsync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rsync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rsync.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rsync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rsync

Przesyłaj pliki do lub ze zdalnego hosta (ale nie pomiędzy dwoma zdalnymi hostami), domyślnie używając SSH.
Aby wskazać na ścieżkę zdalną, użyj `host:ścieżka/do/pliku_lub_katalogu`.
Więcej informacji: <https://download.samba.org/pub/rsync/rsync.1>.

- Prześlij plik:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Użyj trybu archiwum (rekursywnie kopiuj katalogi, kopiuj dowiązania symboliczne bez rozwiązywania i zachowaj uprawnienia, własność i czasy modyfikacji):

`rsync --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Kompresuj dane podczas gdy są wysyłane do miejsca docelowego, wyświetlaj szczegółowy i czytelny dla człowieka postęp i zachowaj częściowo przesłane pliki w przypadku przerwania:

`rsync --compress --verbose --human-readable --partial --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Rekursywnie kopiuj katalogi:

`rsync --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Prześlij zawartość katalogu, ale nie sam katalog:

`rsync --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Rekursywnie kopiuj katalogi, użyj trybu archiwum, rozwiąż dowiązania symboliczne i pomiń pliki, które są nowsze w miejscu docelowym:

`rsync --archive --update --copy-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Prześlij katalog do zdalnego hosta, na którym działa `rsyncd` i usuń pliki w miejscu docelowym które nie istnieją w źródle:

`rsync --recursive --delete rsync://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>

- Prześlij plik poprzez SSH używając innego portu niż domyślny (22) i wyświetlaj globalny postęp:

`rsync --rsh 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_docelowego</span>
