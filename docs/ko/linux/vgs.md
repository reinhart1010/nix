---
layout: page
title: linux/vgs (한국어)
description: "볼륨 그룹에 대한 정보를 표시합니다."
content_hash: f9b0cca161beb95a61894ce9ae4427a9246c9c50
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vgs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vgs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vgs

볼륨 그룹에 대한 정보를 표시합니다.
같이 보기: `lvm`.
더 많은 정보: <https://manned.org/vgs>.

- 볼륨 그룹에 대한 정보 표시:

`vgs`

- 모든 볼륨 그룹 표시:

`vgs -a`

- 기본 표시 항목을 더 자세히 보이도록 변경:

`vgs -v`

- 특정 필드만 표시:

`vgs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름_2</span>

- 기본 표시 항목에 필드를 추가:

`vgs -o +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름</span>

- 제목 줄을 생략:

`vgs --noheadings`

- 필드를 구분자와 함께 구분하여 사용:

`vgs --separator =`
