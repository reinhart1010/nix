---
layout: page
title: common/diff (polski)
description: "Porównaj pliki i foldery."
content_hash: 14d104fc7de28c185e504cb96950f30ce6b2e316
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/diff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/diff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/diff.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diff

Porównaj pliki i foldery.
Więcej informacji: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Porównaj pliki (lista zmian między `stary_plik` a `nowy_plik`):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stary_plik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowy_plik</span>

- Porównaj pliki, ignoruj białe znaki (white spaces):

`diff -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stary_plik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowy_plik</span>

- Porównaj pliki, pokaż różnice obok siebie:

`diff -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stary_plik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowy_plik</span>

- Porównaj pliki, pokaż różnice w ujednoliconym formacie (tak jak w przypadku `git diff`):

`diff -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stary_plik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowy_plik</span>

- Porównaj foldery rekurencyjnie (pokazuje nazwy różniących się plików/folderów a także zmiany w plikach):

`diff -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stary_folder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowy_folder</span>

- Porównaj foldery rekurencyjnie, pokaż tylko nazwy plików które się różnią:

`diff -rq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stary_folder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowy_folder</span>
