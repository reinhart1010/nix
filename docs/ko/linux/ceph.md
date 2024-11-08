---
layout: page
title: linux/ceph (한국어)
description: "통합 스토리지 시스템."
content_hash: fc5d3760294fea2ec1264d2fea9b8849adb61f8f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/ceph.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ceph.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ceph.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ceph

통합 스토리지 시스템.
더 많은 정보: <https://ceph.io/en>.

- 클러스터 상태 확인:

`ceph status`

- 클러스터 사용 통계 확인:

`ceph df`

- 클러스터 내 배치 그룹의 통계 가져오기:

`ceph pg dump --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain</span>

- 스토리지 풀 생성:

`ceph osd pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_번호</span>

- 스토리지 풀 삭제:

`ceph osd pool delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>

- 스토리지 풀 이름 변경:

`ceph osd pool rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_이름</span>

- 풀 스토리지 자체 복구:

`ceph pg repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>
