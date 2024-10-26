---
layout: page
title: common/brew-list (Indonesia)
description: "Tampilkan daftar formula/cask atau berkas-berkas terkait yang terpasang dalam perangkat saat ini."
content_hash: 4e58cfee961ceb7d806637ccd62954c2b206cb37
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/brew-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew-list.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew list

Tampilkan daftar formula/cask atau berkas-berkas terkait yang terpasang dalam perangkat saat ini.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- Tampilkan daftar seluruh formula dan cask yang telah terpasang:

`brew list`

- Tampilkan berkas-berkas yang berasal dari suatu formula yang terpasang:

`brew list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Tampilkan daftar artefak dari suatu cask:

`brew list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask</span>

- Tampilkan daftar formula saja:

`brew list --formula`

- Tampilkan daftar cask saja:

`brew list --cask`
