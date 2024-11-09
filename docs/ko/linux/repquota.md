---
layout: page
title: linux/repquota (한국어)
description: "파일 시스템의 기존 파일 쿼터 요약 정보를 표시합니다."
content_hash: 9604c370108b3f7520c4b382ed5216c87488a6e2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/repquota.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/repquota.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># repquota

파일 시스템의 기존 파일 쿼터 요약 정보를 표시합니다.
더 많은 정보: <https://manned.org/repquota>.

- 사용 중인 모든 쿼터의 통계 보고:

`sudo repquota -all`

- 할당량을 사용하지 않는 사용자도 포함하여 모든 사용자의 쿼터 통계 보고:

`sudo repquota -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템</span>

- 사용자에 대한 쿼터 보고:

`repquota --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템</span>

- 그룹에 대한 쿼터 보고:

`sudo repquota --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템</span>

- 사람이 읽기 쉬운 형식으로 사용된 쿼터 및 제한 보고:

`sudo repquota --human-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템</span>

- 사람이 읽기 쉬운 형식으로 사용자 및 그룹의 모든 쿼터 보고:

`sudo repquota -augs`
