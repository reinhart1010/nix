---
layout: page
title: linux/toolbox-create (한국어)
description: "새 `toolbox` 컨테이너 생성."
content_hash: 00eb1782b8f5f255156fe844b68ea7d32f05916d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/toolbox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox create

새 `toolbox` 컨테이너 생성.
더 많은 정보: <https://manned.org/toolbox-create.1>.

- 특정 배포판에 대한 `toolbox` 컨테이너 생성:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포판</span>

- 현재 배포판의 특정 릴리스에 대한 `toolbox` 컨테이너 생성:

`toolbox create --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">릴리스</span>

- 사용자 지정 이미지로 `toolbox` 컨테이너 생성:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 사용자 지정 Fedora 이미지에서 `toolbox` 컨테이너 생성:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.fedoraproject.org/fedora-toolbox:39</span>

- Fedora 39의 기본 이미지를 사용하여 `toolbox` 컨테이너 생성:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
