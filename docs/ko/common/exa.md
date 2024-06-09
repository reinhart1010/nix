---
layout: page
title: common/exa (한국어)
description: "`ls`의 현대적인 대체품 (디렉토리 내용 나열)."
content_hash: 8a0a80822a66001f04d7b01e939466022d70773b
last_modified_at: 2024-06-09
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/exa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/exa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exa

`ls`의 현대적인 대체품 (디렉토리 내용 나열).
더 많은 정보: <https://the.exa.website>.

- 파일을 한 줄에 하나씩 나열:

`exa --oneline`

- 숨김 파일을 포함한 모든 파일 나열:

`exa --all`

- 모든 파일의 긴 형식 목록 (권한, 소유권, 크기 및 수정 날짜):

`exa --long --all`

- 가장 큰 파일을 맨 위에 나열:

`exa --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- 파일 트리를 3단계 깊이로 표시:

`exa --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 수정 날짜순으로 파일 나열 (오래된 것부터):

`exa --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- 헤더, 아이콘 및 Git 상태와 함께 파일 나열:

`exa --long --header --icons --git`

- `.gitignore`에 언급된 파일은 나열하지 않음:

`exa --git-ignore`
