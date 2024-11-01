---
layout: page
title: common/kubectx (한국어)
description: "`kubectl` 컨텍스트를 관리하고 전환하는 도구."
content_hash: 3dd1684218254df8e042fff9863db621dd6f6356
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectx.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/kubectx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectx

`kubectl` 컨텍스트를 관리하고 전환하는 도구.
더 많은 정보: <https://github.com/ahmetb/kubectx>.

- 컨텍스트 나열:

`kubectx`

- 지정된 이름의 컨텍스트로 전환:

`kubectx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 이전 컨텍스트로 전환:

`kubectx -`

- 지정된 이름의 컨텍스트 이름 변경:

`kubectx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 현재 사용 중인 컨텍스트 표시:

`kubectx -c`

- 지정된 이름의 컨텍스트 삭제:

`kubectx -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
