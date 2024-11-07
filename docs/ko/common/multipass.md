---
layout: page
title: common/multipass (한국어)
description: "네이티브 하이퍼바이저를 사용하여 Ubuntu 가상 머신을 관리."
content_hash: 4aed7f9cf2314e29a80819660512fa9e4aec6189
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/multipass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/multipass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># multipass

네이티브 하이퍼바이저를 사용하여 Ubuntu 가상 머신을 관리.
더 많은 정보: <https://multipass.run/>.

- 인스턴스를 시작할 때 사용할 수 있는 별칭 나열:

`multipass find`

- 새 인스턴스를 시작하고 이름을 설정하고 클라우드-초기화 설정 파일 사용:

`multipass launch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>` --cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일</span>

- 생성된 모든 인스턴스와 일부 속성 나열:

`multipass list`

- 특정 이름의 인스턴스 시작:

`multipass start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>

- 인스턴스의 속성 표시:

`multipass info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>

- 특정 이름의 인스턴스에서 셸 프롬프트 열기:

`multipass shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>

- 이름으로 인스턴스 삭제:

`multipass delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>

- 특정 인스턴스에 디렉토리 마운트:

`multipass mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상/디렉토리</span>
