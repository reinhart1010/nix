---
layout: page
title: common/gh-extension (한국어)
description: "GitHub CLI 확장 관리."
content_hash: 83cba0efbdead3644a9e9060866c46eac918f00d
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-extension.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-extension.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh extension

GitHub CLI 확장 관리.
더 많은 정보: <https://cli.github.com/manual/gh_extension>.

- 동일한 이름의 디렉토리에 새로운 GitHub CLI 확장 프로젝트 초기화:

`gh extension create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_이름</span>

- GitHub 저장소에서 확장 설치:

`gh extension install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- 설치된 확장 나열:

`gh extension list`

- 특정 확장 업그레이드:

`gh extension upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_이름</span>

- 모든 확장 업그레이드:

`gh extension upgrade --all`

- 설치된 확장 나열:

`gh extension list`

- 확장 제거:

`gh extension remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_이름</span>

- 하위 명령에 대한 도움말 표시:

`gh extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
