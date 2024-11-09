---
layout: page
title: linux/rig (한국어)
description: "임의의 이름과 성, 거리 번호와 주소를 생성하는 도구로, 지리적으로 일관된 도시, 주, 우편번호 및 지역번호를 함께 제공합니다."
content_hash: ebee8452454688a3b57aed124ef21cf3600942f5
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/rig.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/rig.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/rig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rig

임의의 이름과 성, 거리 번호와 주소를 생성하는 도구로, 지리적으로 일관된 도시, 주, 우편번호 및 지역번호를 함께 제공합니다.
더 많은 정보: <https://manned.org/rig>.

- 무작위 이름(남성 또는 여성)과 주소 표시:

`rig`

- [m]남성 (또는 [f]여성) 무작위 이름과 주소 표시:

`rig -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m|f</span>

- 특정 [d]디렉터리의 데이터 파일 사용 (기본값은 `/usr/share/rig`):

`rig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 수의 신원 정보 표시:

`rig -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 특정 수의 여성 신원 정보 표시:

`rig -f -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>
