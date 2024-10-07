---
layout: page
title: common/git-sed (한국어)
description: "git으로 관리되는 파일에서 sed를 사용하여 패턴을 대체."
content_hash: 06f970ece38abd203f5ca4d97e59b39c660a2eed
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-sed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-sed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git sed

git으로 관리되는 파일에서 sed를 사용하여 패턴을 대체.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>.

- 현재 저장소에서 지정된 텍스트 대체:

`git sed '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_텍스트</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_텍스트</span>`'`

- 지정된 텍스트를 대체한 후, 표준 커밋 메시지로 결과 변경사항 커밋:

`git sed -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_텍스트</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_텍스트</span>`'`

- 정규 표현식을 사용하여 지정된 텍스트 대체:

`git sed -f g '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_텍스트</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_텍스트</span>`'`

- 주어진 디렉터리 내 모든 파일에서 특정 텍스트 대체:

`git sed '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_텍스트</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_텍스트</span>`' -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
