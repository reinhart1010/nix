---
layout: page
title: linux/pkgmk (한국어)
description: "CRUX에서 pkgadd로 사용할 바이너리 패키지를 만듭니다."
content_hash: 774d0f4bc73396856b619840f167b959efc1f094
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pkgmk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkgmk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkgmk

CRUX에서 pkgadd로 사용할 바이너리 패키지를 만듭니다.
더 많은 정보: <https://docs.oracle.com/cd/E88353_01/html/E37839/pkgmk-1.html>.

- 패키지 만들기 및 다운로드:

`pkgmk -d`

- 패키지 생성 후 설치:

`pkgmk -d -i`

- 패키지 생성 후 업그레이드:

`pkgmk -d -u`

- 패키지 생성 시 발자국 무시:

`pkgmk -d -if`

- 패키지 생성 시 MD5 합계 무시:

`pkgmk -d -im`

- 패키지의 발자국 업데이트:

`pkgmk -uf`
