---
layout: page
title: common/crictl (한국어)
description: "CRI 호환 컨테이너 런타임을 위한 커멘드라인."
content_hash: db7b8943fb54a4345bece1eec618d2f8500f4a36
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crictl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crictl

CRI 호환 컨테이너 런타임을 위한 커멘드라인.
더 많은 정보: <https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>.

- 모든 kubernetes 파드 나열 (준비 및 준비되지 않음):

`crictl pods`

- 모든 컨테이너 나열 (실행 중 및 종료):

`crictl ps --all`

- 모든 이미지 나열:

`crictl images`

- 특정 컨테이너들 정보 표시:

`crictl inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_아이디1 컨테이너_아이디2 ...</span>

- 실행 중인 컨테이너 내에서 특정 셸을 열기:

`crictl exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- 레지스트리에서 특정 이미지를 가져옴:

`crictl pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- 특정 컨테이너의 로그를 출력하고 추적([f]ollow):

`crictl logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_아이디</span>

- 하나 이상의 이미지를 제거:

`crictl rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_아이디1 이미지_아이디2 ...</span>
