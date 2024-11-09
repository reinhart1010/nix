---
layout: page
title: linux/distrobox-create (한국어)
description: "Distrobox 컨테이너 생성. 같이 보기: `tldr distrobox`."
content_hash: 97602b8854ed8b6610560405387827823df7273e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-create.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-create

Distrobox 컨테이너 생성. 같이 보기: `tldr distrobox`.
생성된 컨테이너는 호스트와 밀접하게 통합되어 사용자의 HOME 디렉토리, 외부 저장소, 외부 USB 장치, 그래픽 애플리케이션(X11/Wayland), 오디오를 공유할 수 있습니다.
더 많은 정보: <https://distrobox.it/usage/distrobox-create>.

- Ubuntu 이미지로 Distrobox 컨테이너 생성:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Distrobox 컨테이너 복제:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">복제된_컨테이너_이름</span>
