---
layout: page
title: common/gh-help (한국어)
description: "GitHub CLI 명령에 대한 도움말 표시."
content_hash: de9d5294836fa07326dd2ca435a4e0d84814a4a5
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-help.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-help.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh help

GitHub CLI 명령에 대한 도움말 표시.
더 많은 정보: <https://cli.github.com/manual/gh_help>.

- 일반 도움말 표시:

`gh help`

- `gh help` 하위 명령에 대한 도움말 표시:

`gh help --help`

- `gh`와 함께 사용할 수 있는 환경 변수에 대한 도움말 표시:

`gh help environment`

- 모든 `gh` 명령의 마크다운 참고 자료 표시:

`gh help reference`

- `jq`를 사용하여 `gh`의 JSON 출력 형식을 지정하는 방법에 대한 도움말 표시:

`gh help formatting`

- MinTTY와 함께 `gh`를 사용하는 방법에 대한 도움말 표시:

`gh help mintty`

- 하위 명령에 대한 도움말 표시:

`gh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>

- 하위 명령 작업에 대한 도움말 표시:

`gh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">create</span>
