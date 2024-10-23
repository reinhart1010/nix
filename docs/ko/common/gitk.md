---
layout: page
title: common/gitk (한국어)
description: "Git 저장소를 그래픽으로 탐색."
content_hash: 9304990fde0edb58ce2e2ccc10a24a1bab0e882d
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitk

Git 저장소를 그래픽으로 탐색.
참고: `git-gui`, `git-cola`, `tig`.
더 많은 정보: <https://git-scm.com/docs/gitk>.

- 현재 Git 저장소에 대한 저장소 브라우저를 표시:

`gitk`

- 특정 파일이나 디렉토리에 대한 저장소 브라우저 표시:

`gitk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>

- 1주일 전 이후에 이루어진 커밋 표시:

`gitk --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 week ago</span>`"`

- 2016년 1월 1일보다 오래된 커밋을 표시:

`gitk --until="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1/1/2015</span>`"`

- 모든 지점에서 최대 100개의 변경 사항 표시:

`gitk --max-count=100 --all`
