---
layout: page
title: linux/ctr (한국어)
description: "`containerd` 컨테이너 및 이미지 관리."
content_hash: f29d68c92788178aaeb920b31551e31a1d98228d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ctr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ctr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ctr

`containerd` 컨테이너 및 이미지 관리.
더 많은 정보: <https://containerd.io>.

- 모든 컨테이너 나열 (실행 중 및 중지됨):

`ctr containers list`

- 모든 이미지 나열:

`ctr images list`

- 이미지 다운로드:

`ctr images pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 이미지 태그 지정:

`ctr images tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_태그</span>
