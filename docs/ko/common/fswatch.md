---
layout: page
title: common/fswatch (한국어)
description: "크로스 플랫폼 파일 변경 모니터."
content_hash: 8ca7883706a0e8e8b22b3c9a21fc316a9411ddd5
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fswatch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fswatch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fswatch

크로스 플랫폼 파일 변경 모니터.
더 많은 정보: <https://emcrisostomo.github.io/fswatch>.

- 파일 생성, 업데이트 또는 삭제 시 Bash 명령을 실행:

`fswatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | xargs -n 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash_명령어</span>

- 하나 이상의 파일 또는 디렉터리를 감시:

`fswatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/another_directory/**/*.js</span>` | xargs -n 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash_명령어</span>

- 변경된 파일의 절대 경로를 출력:

`fswatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` | xargs -n 1 -I {} echo {}`

- 이벤트 유형 별로 필터링:

`fswatch --event `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Updated|Deleted|Created</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` | xargs -n 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash_명령어</span>
