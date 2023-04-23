---
layout: page
title: common/rsync (polski)
description: "Przesyłaj pliki do lub ze zdalnego hosta (ale nie pomiędzy dwoma zdalnymi hostami)."
content_hash: a5795f842249ae7559bab611479971d0753a5f2c
last_modified_at: 2023-04-23
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
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rsync

Przesyłaj pliki do lub ze zdalnego hosta (ale nie pomiędzy dwoma zdalnymi hostami).
Może przesyłać pojedyncze pliki lub wiele plików pasujących do wzorca.
Więcej informacji: <https://manned.org/rsync>.

- Prześlij plik z lokalnego do zdalnego hosta:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_katalogu</span>

- Prześlij plik ze zdalnego do lokalnego hosta:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu</span>

- Prześlij plik w trybie [a]rchiwum (aby zachować atrybuty) i skompresowanym ([z]ip) wyświetlając szczegółowy ([v]erbose) i czytelny dla człowieka ([h]uman-readable) [P]ostęp:

`rsync -azvhP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_katalogu</span>

- Prześlij katalog i jego zawartość ze zdalnego do lokalnego hosta:

`rsync -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu</span>

- Prześlij zawartość katalogu (ale nie sam katalog) ze zdalnego do lokalnego hosta:

`rsync -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_katalogu</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu</span>

- Prześlij katalog [r]ekursywnie, w trybie [a]rchiwum (aby zachować atrybuty), rozwiązując zawarte dowiązania symbo[L]iczne, i ignorując już przesłane pliki o ile nie są nowsze ([u]nless):

`rsync -rauL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu</span>

- Prześlij plik poprzez SSH i usuń pliki na zdalnym hoście, które nie istnieją na lokalnym:

`rsync -e ssh --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_pliku</span>

- Prześlij pliki poprzez SSH używając innego portu niż domyślny i wyświetlaj globalny postęp:

`rsync -e 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdalny_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/zdalnego_pliku</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_pliku</span>
