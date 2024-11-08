---
layout: page
title: linux/dropbearconvert (한국어)
description: "Dropbear와 OpenSSH 개인 키 형식 간 변환."
content_hash: ab53f95e86647600b32e7cba3bad5471a431df76
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dropbearconvert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dropbearconvert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dropbearconvert

Dropbear와 OpenSSH 개인 키 형식 간 변환.
더 많은 정보: <https://manned.org/dropbearconvert.1>.

- OpenSSH 개인 키를 Dropbear 형식으로 변환:

`dropbearconvert openssh dropbear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_키</span>

- Dropbear 개인 키를 OpenSSH 형식으로 변환:

`dropbearconvert dropbear openssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_키</span>
