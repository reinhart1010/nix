---
layout: page
title: common/docker-tag (한국어)
description: "기존 Docker 이미지에 태그를 지정합니다."
content_hash: aec5d0a4ac1bd1fa6f73701dc1aff0dc694e6875
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/docker-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker tag

기존 Docker 이미지에 태그를 지정합니다.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/tag/>.

- 특정 이미지 ID에 이름과 태그 지정:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 특정 이미지에 태그 지정:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_태그</span>

- 도움말 표시:

`docker tag`
