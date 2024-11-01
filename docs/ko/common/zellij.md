---
layout: page
title: common/zellij (한국어)
description: "배터리가 포함된 터미널 멀티플렉서."
content_hash: 338db32a51a32315ac69e9582157258d0cad9ed3
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zellij.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zellij.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zellij

배터리가 포함된 터미널 멀티플렉서.
같이 보기: `tmux` 및 `screen`.
더 많은 정보: <https://zellij.dev/documentation/>.

- 새 세션 시작:

`zellij --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 기존 세션 목록:

`zellij list-sessions`

- 가장 최근에 사용한 세션에 연결:

`zellij attach`

- 새 창 열기 (zellij 세션 내):

`<Alt> + N`

- 현재 세션에서 분리 (zellij 세션 내):

`<Ctrl> + O, D`
