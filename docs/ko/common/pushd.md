---
layout: page
title: common/pushd (한국어)
description: "디렉터리를 스택에 쌓아 나중에 접근할 수 있도록 합니다."
content_hash: 31e803bcaf2704ea6097907814ed11b645f05e9a
last_modified_at: 2024-11-07
related_topics:
  - title: dansk version
    url: /da/common/pushd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pushd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pushd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pushd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pushd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pushd

디렉터리를 스택에 쌓아 나중에 접근할 수 있도록 합니다.
원래 디렉터리로 돌아가려면 `popd`, 디렉터리 스택 내용을 보려면 `dirs`를 같이 보세요.
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- 디렉터리로 이동하고 스택에 추가:

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 스택의 첫 번째와 두 번째 디렉터리를 전환:

`pushd`

- 스택을 회전하여 5번째 요소를 스택의 맨 위로:

`pushd +4`

- 스택을 왼쪽으로 4번 회전 (현재 디렉터리는 5번째 요소를 교체하여 맨 위에 유지):

`pushd -n +4`
