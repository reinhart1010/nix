---
layout: page
title: common/vimdiff (한국어)
description: "두 개 이상의 파일을 vim으로 열어 차이점을 보여줍니다."
content_hash: ae182c997a146761648cc8c880722753651204b8
last_modified_at: 2024-11-03
related_topics:
  - title: Deutsch version
    url: /de/common/vimdiff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vimdiff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vimdiff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vimdiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vimdiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vimdiff

두 개 이상의 파일을 vim으로 열어 차이점을 보여줍니다.
같이 보기: `vim`, `vimtutor`, `nvim`.
더 많은 정보: <https://www.vim.org>.

- 두 파일을 열고 차이점 표시:

`vimdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 커서를 왼쪽|오른쪽 창으로 이동:

`<Ctrl> + w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|l</span>

- 이전 차이점으로 이동:

`[c`

- 다음 차이점으로 이동:

`]c`

- 강조 표시된 차이점을 다른 창에서 현재 창으로 복사:

`do`

- 강조 표시된 차이점을 현재 창에서 다른 창으로 복사:

`dp`

- 모든 강조 표시 및 접기 업데이트:

`:diffupdate`

- 강조 표시된 코드 접기 전환:

`za`
