---
layout: page
title: linux/pvs (한국어)
description: "물리 볼륨에 대한 정보를 표시합니다."
content_hash: f81724a5f41b71a00c417e06918782321eb81c24
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pvs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pvs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pvs

물리 볼륨에 대한 정보를 표시합니다.
같이 보기: `lvm`.
더 많은 정보: <https://manned.org/pvs>.

- 물리 볼륨에 대한 정보 표시:

`pvs`

- 비물리적 볼륨 표시:

`pvs -a`

- 기본 표시를 자세히 보여주도록 변경:

`pvs -v`

- 특정 필드만 표시:

`pvs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름_2</span>

- 기본 표시에 필드를 추가:

`pvs -o +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름</span>

- 헤딩 행 생략:

`pvs --noheadings`

- 필드 구분자 사용:

`pvs --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">특수_문자</span>
