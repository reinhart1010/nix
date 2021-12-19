---
layout: page
title: common/balena (한국어)
description: "명령 줄에서 balenaCloud, openBalena 및 balena API와 상호 작용하십시오."
content_hash: fb8b99571657514e59435a98bb27965b8e0771f8
related_topics:
  - title: English version
    url: /en/common/balena.html
    icon: bi bi-globe
---
# balena

명령 줄에서 balenaCloud, openBalena 및 balena API와 상호 작용하십시오.
더 많은 정보: <https://www.balena.io/docs/reference/cli/>.

- balenaCloud 계정에 로그인:

`balena login`

- BalencaCloud 또는 OpenBalena 애플리케이션 생성:

`balena app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- 계정 내 모든 balenaCloud 또는 openBalena 애플리케이션 나열:

`balena apps`

- balenaCloud 또는 openBalena 계정과 관련된 모든 장치 나열:

`balena devices`

- BalenaOS 이미지를 로컬 드라이브에 플래시:

`balena local flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/balenaos.img</span>` --drive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_location</span>
