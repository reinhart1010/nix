---
layout: page
title: common/git-difftool (한국어)
description: "외부 diff 도구를 사용하여 파일 변경 사항을 표시합니다. `git diff`와 동일한 옵션과 인수를 허용합니다."
content_hash: 0b0bb395640af58fa9937d1801f95ee116aa17c4
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-difftool.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-difftool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-difftool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-difftool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-difftool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git difftool

외부 diff 도구를 사용하여 파일 변경 사항을 표시합니다. `git diff`와 동일한 옵션과 인수를 허용합니다.
같이 보기: `git diff`.
더 많은 정보: <https://git-scm.com/docs/git-difftool>.

- 사용 가능한 diff 도구 나열:

`git difftool --tool-help`

- 기본 diff 도구를 meld로 설정:

`git config --global diff.tool "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meld</span>`"`

- 기본 diff 도구를 사용하여 스테이징된 변경 사항 표시:

`git difftool --staged`

- 특정 도구(opendiff)를 사용하여 주어진 커밋 이후의 변경 사항 표시:

`git difftool --tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opendiff</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>
