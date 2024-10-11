---
layout: page
title: common/clido (한국어)
description: "터미널용 상태 저장 TODO 앱."
content_hash: 5768b288fe190d4451d0d79b2b1b1fe9138ff857
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/clido.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clido.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clido

터미널용 상태 저장 TODO 앱.
더 많은 정보: <https://codeberg.org/Oglo12/clido/wiki>.

- 목록 생성:

`clido --new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 목록 로드:

`clido --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 목록 삭제:

`clido --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 모든 목록 나열:

`clido --lists`

- 자동쓰기 전환:

`clido toggle-autowrite`

- 텍스트 편집기에서 목록을 열기:

`clido edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트_편집기</span>

- 도움말 표시:

`clido -h`

- 버전 정보 표시:

`clido -v`
