---
layout: page
title: common/expand (한국어)
description: "탭을 공백으로 변환."
content_hash: 0173b8918d20fec49305c55e2687be1c8ae82c78
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/expand.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/expand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/expand.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/expand.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># expand

탭을 공백으로 변환.
더 많은 정보: <https://www.gnu.org/software/coreutils/expand>.

- 각 파일의 탭을 공백으로 변환하여 `stdout`에 작성:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 읽어 탭을 공백으로 변환:

`expand`

- 공백이 아닌 경우 탭을 변환하지 않음:

`expand -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 탭을 8자가 아닌 특정 수의 문자 간격으로 위치:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 명시적인 탭 위치를 쉼표로 구분한 목록을 사용:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>
