---
layout: page
title: common/pastel (한국어)
description: "색상을 생성, 분석, 변환 및 조작."
content_hash: 61ae272c123b2056e34660584f0b45cd22d29d42
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pastel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pastel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pastel

색상을 생성, 분석, 변환 및 조작.
더 많은 정보: <https://github.com/sharkdp/pastel>.

- 색상을 한 형식에서 다른 형식으로 변환. 여기서는 RGB에서 HSL로 변환:

`pastel format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hsl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff8000</span>

- 터미널에서 색상을 표시하고 분석:

`pastel color "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rgb(255,50,127)</span>`"`

- 화면에서 색상 선택:

`pastel pick`

- 시각적으로 구별되는 N개의 색상 세트 생성:

`pastel distinct `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>

- 모든 X11/CSS 색상 이름 나열:

`pastel list`
