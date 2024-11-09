---
layout: page
title: linux/hlint (한국어)
description: "Haskell 코드에 대한 개선 사항을 제안합니다."
content_hash: 3fc7ed3edba5a74077a400188f2f5a0dfea6f96d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/hlint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hlint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hlint

Haskell 코드에 대한 개선 사항을 제안합니다.
더 많은 정보: <https://hackage.haskell.org/package/hlint>.

- 주어진 파일에 대한 제안 사항 표시:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` options`

- 모든 Haskell 파일을 검사하고 보고서 생성:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --report`

- 대부분의 제안을 자동으로 적용:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --refactor`

- 추가 옵션 표시:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --refactor-options`

- 모든 미해결 힌트를 무시하는 설정 파일 생성:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --default > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.hlint.yaml</span>
