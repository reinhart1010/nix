---
layout: page
title: common/nvm.fish (한국어)
description: "fish 셸에서 Node.js 버전을 설치, 제거 또는 전환."
content_hash: c4aac9737cee5277e9034c05315fdf612c3239f9
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nvm.fish.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nvm.fish.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvm

fish 셸에서 Node.js 버전을 설치, 제거 또는 전환.
"12.8" 또는 "v16.13.1"과 같은 버전 번호 및 "stable", "system" 등의 레이블을 지원.
더 많은 정보: <https://github.com/jorgebucaran/nvm.fish>.

- 특정 버전의 Node.js 설치:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 현재 셸에서 특정 버전의 Node.js 사용:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 기본 Node.js 버전 설정:

`set nvm_default_version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 사용 가능한 모든 Node.js 버전 나열 및 기본 버전 강조:

`nvm list`

- 지정된 Node.js 버전 제거:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>
