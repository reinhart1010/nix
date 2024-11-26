---
layout: page
title: linux/libtoolize (한국어)
description: "`autotools` 도구로, `libtool`을 사용하기 위해 패키지를 준비합니다."
content_hash: 40e252e0d2bebe81afe4030f900bbe28b5e643f2
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/linux/libtoolize.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/libtoolize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libtoolize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libtoolize

`autotools` 도구로, `libtool`을 사용하기 위해 패키지를 준비합니다.
여러 작업을 수행하며, 필요한 파일 및 디렉토리를 생성하여 `libtool`을 프로젝트에 원활하게 통합합니다.
더 많은 정보: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- `libtool`을 필요한 파일을 복사하여(심볼릭 링크는 피함) 프로젝트를 초기화하고 필요한 경우 기존 파일을 덮어씀:

`libtoolize --copy --force`
