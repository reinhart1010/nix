---
layout: page
title: linux/rankmirrors (한국어)
description: "Pacman 미러 목록을 연결 및 열기 속도에 따라 순위 매기기."
content_hash: a83bc8468f67de3b869ce9e25fd2fc8abe09e187
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rankmirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rankmirrors

Pacman 미러 목록을 연결 및 열기 속도에 따라 순위 매기기.
새로운 미러리스트를 `stdout`에 작성합니다.
더 많은 정보: <https://manned.org/rankmirrors>.

- 미러 목록 순위 매기기:

`rankmirrors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- 상위 순위 서버의 지정된 개수만 출력:

`rankmirrors -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- 미러리스트 생성 시 자세히 출력:

`rankmirrors -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- 특정 URL만 테스트:

`rankmirrors --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- 전체 미러리스트 대신 응답 시간만 출력:

`rankmirrors --times `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>
