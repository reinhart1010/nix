---
layout: page
title: common/eza (한국어)
description: "`exa`를 기반으로 한 `ls`의 현대적이고 유지 관리되는 대체품."
content_hash: dd2901a959dc6e2fc459fddb683da83a6b0dfd07
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/eza.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/eza.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/eza.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/eza.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eza

`exa`를 기반으로 한 `ls`의 현대적이고 유지 관리되는 대체품.
더 많은 정보: <https://github.com/eza-community/eza>.

- 파일을 한 줄에 하나씩 나열:

`eza --oneline`

- 숨김 파일을 포함한 모든 파일 나열:

`eza --all`

- 모든 파일의 긴 형식 목록 (권한, 소유권, 크기 및 수정 날짜):

`eza --long --all`

- 가장 큰 파일을 맨 위에 나열:

`eza --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- 파일 트리를 3단계 깊이로 표시:

`eza --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 수정 날짜순으로 파일 나열 (오래된 것부터):

`eza --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- 헤더, 아이콘 및 Git 상태와 함께 파일 나열:

`eza --long --header --icons --git`

- `.gitignore`에 언급된 파일은 나열하지 않음:

`eza --git-ignore`
