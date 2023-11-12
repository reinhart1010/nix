---
layout: page
title: common/bosh (한국어)
description: "bosh 디렉터를 배치 및 관리하기 위한 커맨드라인 도구."
content_hash: a007971cf4f3a31d6d79d95bc1fd305e7bd76e23
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bosh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bosh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bosh

bosh 디렉터를 배치 및 관리하기 위한 커맨드라인 도구.
더 많은 정보: <https://bosh.io/docs/cli-v2/>.

- 디렉터의 로컬 별칭 생성:

`bosh alias-env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경명</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소|url</span>` --ca-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_증명서</span>

- 환경 나열:

`bosh environments`

- 디렉터에 로그인:

`bosh login -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>

- 배포 목록 나열:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>` deployments`

- 가상 머신 환경 나열:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>` vms -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전개</span>

- 가상 머신의 ssh:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전개</span>

- stemcell 업로드:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>` upload-stemcell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stemcell_파일|url</span>

- 현재 클라우드 구성 표시:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>` cloud-config`
