---
layout: page
title: linux/bleachbit (한국어)
description: "파일 시스템의 불필요한 파일을 정리합니다."
content_hash: 01bef5ccaea3932345a32fec2a8ab0f1e75339d8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/bleachbit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/bleachbit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bleachbit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bleachbit

파일 시스템의 불필요한 파일을 정리합니다.
더 많은 정보: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Bleachbit의 그래픽 사용자 인터페이스(GUI) 버전 시작:

`bleachbit --gui`

- 파일 삭제:

`bleachbit --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용 가능한 클리너 옵션 나열:

`bleachbit --list-cleaners`

- 정리 작업을 실제로 수행하기 전에 삭제될 파일 및 변경 사항 미리 보기:

`bleachbit --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- 정리 작업 수행 및 파일 삭제:

`bleachbit --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
