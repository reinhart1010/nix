---
layout: page
title: common/doctl-compute-droplet (한국어)
description: "드롭릿이라고 불리는 가상 머신을 나열, 생성, 삭제."
content_hash: b136b9b3a079febcefe489212a0a44b158365254
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-compute-droplet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl compute droplet

드롭릿이라고 불리는 가상 머신을 나열, 생성, 삭제.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>.

- 드롭릿 생성:

`doctl compute droplet create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os_이미지</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vps_타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드롭릿_이름</span>

- 드롭릿 삭제:

`doctl compute droplet delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드롭릿_아이디|드롭릿_이름</span>

- 드롭릿 나열:

`doctl compute droplet list`
