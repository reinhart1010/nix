---
layout: page
title: linux/xinput (한국어)
description: "사용 가능한 입력 장치를 나열하고, 장치에 대한 정보를 쿼리하며, 입력 장치 설정을 변경."
content_hash: c3d7e78d96e8e2dfb19f05ef0bc47783d34c167e
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xinput.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xinput

사용 가능한 입력 장치를 나열하고, 장치에 대한 정보를 쿼리하며, 입력 장치 설정을 변경.
더 많은 정보: <https://manned.org/xinput>.

- 모든 입력 장치 나열:

`xinput list`

- 입력 장치 비활성화:

`xinput disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 입력 장치 활성화:

`xinput enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 입력 장치를 마스터에서 분리:

`xinput float `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 입력 장치를 슬레이브로 마스터에 재연결:

`xinput reattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마스터_id</span>

- 입력 장치의 설정 나열:

`xinput list-props `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 입력 장치의 설정 변경:

`xinput set-prop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
