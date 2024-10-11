---
layout: page
title: common/gh-completion (한국어)
description: "GitHub CLI 명령어에 대한 셸 자동완성 스크립트 생성."
content_hash: 93d43b5856f9f1cc173eced9b128b758f46e6083
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-completion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-completion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh completion

GitHub CLI 명령어에 대한 셸 자동완성 스크립트 생성.
더 많은 정보: <https://cli.github.com/manual/gh_completion>.

- 자동완성 스크립트 출력:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish|powershell</span>

- `gh` 자동완성 스크립트를 `~/.bashrc`에 추가:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.bashrc</span>

- `gh` 자동완성 스크립트를 `~/.zshrc`에 추가:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zshrc</span>

- 하위 명령어 도움말 표시:

`gh completion`
