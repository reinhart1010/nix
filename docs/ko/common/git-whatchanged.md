---
layout: page
title: common/git-whatchanged (한국어)
description: "최근 커밋 또는 파일의 변경 사항을 보여줍니다."
content_hash: 78f690c5bfc86ded9b34e05cdc3aae928b581182
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-whatchanged.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-whatchanged.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git whatchanged

최근 커밋 또는 파일의 변경 사항을 보여줍니다.
같이 보기: `git log`.
더 많은 정보: <https://git-scm.com/docs/git-whatchanged>.

- 최근 커밋의 로그와 변경 사항 표시:

`git whatchanged`

- 지정된 시간 범위 내에서 최근 커밋의 로그와 변경 사항 표시:

`git whatchanged --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 hours ago</span>`"`

- 특정 파일 또는 디렉토리에 대한 최근 커밋의 로그와 변경 사항 표시:

`git whatchanged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
