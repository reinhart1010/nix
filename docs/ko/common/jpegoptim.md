---
layout: page
title: common/jpegoptim (한국어)
description: "JPEG 이미지 최적화 도구."
content_hash: 88ef14fe79f7b318d8354c5debbaee63610eea69
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jpegoptim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jpegoptim

JPEG 이미지 최적화 도구.
더 많은 정보: <https://github.com/tjko/jpegoptim>.

- 모든 관련 데이터를 유지하며 JPEG 이미지 집합 최적화:

`jpegoptim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지N.jpeg</span>

- 모든 비필수 데이터를 제거하며 JPEG 이미지 최적화:

`jpegoptim --strip-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지N.jpeg</span>

- 출력 이미지를 프로그레시브 형식으로 강제 변환:

`jpegoptim --all-progressive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지N.jpeg</span>

- 출력 이미지의 최대 파일 크기를 고정:

`jpegoptim --size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">250k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지N.jpeg</span>
