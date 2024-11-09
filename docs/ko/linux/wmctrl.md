---
layout: page
title: linux/wmctrl (한국어)
description: "X 윈도우 매니저용 CLI."
content_hash: cfe8a2954748f62220ea033ea92f397d27dfbb94
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wmctrl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/wmctrl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wmctrl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wmctrl

X 윈도우 매니저용 CLI.
더 많은 정보: <https://manned.org/wmctrl>.

- 윈도우 매니저가 관리하는 모든 창 나열:

`wmctrl -l`

- (부분적으로) 제목이 일치하는 첫 번째 창으로 전환:

`wmctrl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">창_제목</span>

- 창을 현재 작업공간으로 이동하고, 올려서 포커스를 줌:

`wmctrl -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">창_제목</span>

- 작업공간으로 전환:

`wmctrl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업공간_번호</span>

- 창을 선택하고 전체 화면 전환:

`wmctrl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">창_제목</span>` -b toggle,fullscreen`

- 창을 선택하고 작업공간으로 이동:

`wmctrl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">창_제목</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업공간_번호</span>
