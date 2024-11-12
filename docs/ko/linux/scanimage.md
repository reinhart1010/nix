---
layout: page
title: linux/scanimage (한국어)
description: "Scanner Access Now Easy API를 사용하여 이미지를 스캔."
content_hash: a14806f86ee53d269851c794126a7f69f3381c40
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/scanimage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scanimage

Scanner Access Now Easy API를 사용하여 이미지를 스캔.
더 많은 정보: <http://sane-project.org/man/scanimage.1.html>.

- 사용 가능한 스캐너를 나열하여 대상 장치가 연결되고 인식되었는지 확인:

`scanimage -L`

- 이미지를 스캔하여 파일로 저장:

`scanimage --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pnm|tiff|png|jpeg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_이미지</span>
