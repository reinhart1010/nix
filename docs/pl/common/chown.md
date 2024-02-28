---
layout: page
title: common/chown (polski)
description: "Zmienia właściciela i grupę właścicieli dla plików i katalogów."
content_hash: b3afa6f07d91ac268deb7b6206ad8402ae668f6e
last_modified_at: 2024-02-28
related_topics:
  - title: Deutsch version
    url: /de/common/chown.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chown.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chown.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chown.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chown.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chown.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chown

Zmienia właściciela i grupę właścicieli dla plików i katalogów.
Więcej informacji: <https://www.gnu.org/software/coreutils/chown>.

- Zmień właściciela pliku/katalogu:

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Zmień właściciela i grupę właścicieli pliku/katalogu:

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Rekursywnie zmień właściciela katalogu i jego zawartości:

`chown -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>

- Zmień właściciela dowiązania symbolicznego:

`chown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/dowiązania_symbolicznego</span>

- Zmień właściciela pliku/katalogu by był taki sam jak w pliku referencyjnym:

`chown --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_referencyjnego</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>
