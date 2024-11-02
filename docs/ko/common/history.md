---
layout: page
title: common/history (한국어)
description: "커멘드 라인 히스토리."
content_hash: 18aa5186747c4f728670d6478a2eee7a62123c59
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/history.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/history.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># history

커멘드 라인 히스토리.
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- 줄 번호와 함께 명령 기록 목록을 표시:

`history`

- 마지막 20개의 명령을 표시 (Zsh에서는 20번째부터 시작하는 모든 명령을 표시):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- 다양한 형식의 타임스탬프가 포함된 기록을 표시 (Zsh에서만 사용 가능):

`history -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|f|i|E</span>

- 명령 기록 목록을 삭제([c]lear) (현재 Bash 쉘에만 해당):

`history -c`

- 현재 Bash 쉘의 기록으로 기록 파일 덮어쓰기(Over[w]rite) (종종 기록을 제거하기 위해 `history -c`와 결합되어 사용):

`history -w`

- 지정된 오프셋에서 기록 항목을 삭제([d]elete):

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오프셋</span>
