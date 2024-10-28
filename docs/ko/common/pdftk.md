---
layout: page
title: common/pdftk (한국어)
description: "PDF 도구 모음."
content_hash: 85ca99122f133d687406b70bae6851a22a42e0eb
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/pdftk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pdftk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pdftk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdftk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdftk

PDF 도구 모음.
더 많은 정보: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>.

- PDF 파일에서 1-3, 5, 6-10 페이지를 추출하여 다른 파일로 저장:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3 5 6-10</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- PDF 파일 목록을 병합(연결)하여 결과를 다른 파일로 저장:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.pdf 파일2.pdf ...</span>` cat output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- PDF 파일의 각 페이지를 별도의 파일로 분할하고, 지정된 파일 이름 출력 패턴 사용:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.pdf</span>` burst output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_%d.pdf</span>

- 모든 페이지를 시계 방향으로 180도 회전:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-endsouth</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- 세 번째 페이지만 시계 방향으로 90도 회전하고 나머지는 변경 없이 유지:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-2 3east 4-end</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>
