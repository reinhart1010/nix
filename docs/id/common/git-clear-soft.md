---
layout: page
title: common/git-clear-soft (Indonesia)
description: "Hapus direktori kerja Git tidak termasuk file di `.gitignore`, seolah-olah baru saja dikloning dengan cabang saat ini."
content_hash: 5794efc384c840591bdaef4f900c106e32a850f2
last_modified_at: 2024-05-03
related_topics:
  - title: English version
    url: /en/common/git-clear-soft.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-clear-soft.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git clear-soft

Hapus direktori kerja Git tidak termasuk file di `.gitignore`, seolah-olah baru saja dikloning dengan cabang saat ini.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-clear-soft>.

- Reset semua file yang terlacak dan hapus semua file yang tidak terlacak:

`git clear-soft`
