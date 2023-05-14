---
layout: page
title: linux/unsquashfs (polski)
description: "Dekompresuj, rozpakuj i wyświetl listę plików w systemach plików squashfs."
content_hash: 8669f573a9611fe9cbb46b0e2be47002849e9082
last_modified_at: 2023-05-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unsquashfs

Dekompresuj, rozpakuj i wyświetl listę plików w systemach plików squashfs.
Więcej informacji: <https://manned.org/unsquashfs>.

- Rozpakuj system plików squashfs do `squashfs-root` w aktualnym katalogu roboczym:

`unsquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Rozpakuj system plików squashfs do podanego katalogu:

`unsquashfs -dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Wyświetlaj nazwy plików podczas ich rozpakowywania:

`unsquashfs -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Wyświetlaj nazwy plików i ich atrybuty podczas ich rozpakowywania:

`unsquashfs -linfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Wyświetl listę plików w systemie plików squashfs (bez rozpakowywania):

`unsquashfs -ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>

- Wyświetl listę plików i ich atrybuty w systemie plików squashfs (bez rozpakowywania):

`unsquashfs -lls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_plików.squashfs</span>
