---
layout: page
title: common/set (한국어)
description: "셸 옵션을 토글하거나 위치 매개변수의 값을 설정."
content_hash: 7e74df761d7923e26b30ee51aab0052005ce5671
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/set.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/set.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># set

셸 옵션을 토글하거나 위치 매개변수의 값을 설정.
더 많은 정보: <https://manned.org/set.1posix>.

- 셸 변수의 이름과 값을 표시:

`set`

- 새로 초기화된 변수를 자식 프로세스에 내보내기:

`set -a`

- 작업이 완료될 때 `stderr`에 형식화된 메시지 쓰기:

`set -b`

- `vi`와 유사한 키 바인딩(e.g. `yy`)으로 명령줄에서 텍스트 쓰기 및 편집:

`set -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vi</span>

- 기본 모드로 돌아가기:

`set -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>

- 모든 모드 나열:

`set -o`

- (일부) 명령이 실패할 때 셸 종료:

`set -e`
