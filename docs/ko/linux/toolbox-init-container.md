---
layout: page
title: linux/toolbox-init-container (한국어)
description: "실행 중인 `toolbox` 컨테이너를 초기화합니다."
content_hash: 1d592ef03e143b2337d0f27a9c7684ed4a3ab602
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/toolbox-init-container.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-init-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox init-container

실행 중인 `toolbox` 컨테이너를 초기화합니다.
이 명령은 사용자가 실행해서는 안 되며, 호스트에서 실행할 수 없습니다.
더 많은 정보: <https://manned.org/toolbox-init-container.1>.

- 실행 중인 toolbox 초기화:

`toolbox init-container --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid</span>` --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">home</span>` --home-link --media-link --mnt-link --monitor-host --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>` --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
