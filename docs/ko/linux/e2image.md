---
layout: page
title: linux/e2image (한국어)
description: "ext2/ext3/ext4 파일 시스템의 중요한 메타데이터를 파일로 저장."
content_hash: 808a34fdf147574d615bf7e37ec713ad2c3c16c6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/e2image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# e2image

ext2/ext3/ext4 파일 시스템의 중요한 메타데이터를 파일로 저장.
더 많은 정보: <https://manned.org/e2image>.

- 장치에 있는 메타데이터를 특정 파일에 기록:

`e2image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 장치에 있는 메타데이터를 `stdout`에 출력:

`e2image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` -`

- 파일 시스템 메타데이터를 장치로 복원:

`e2image -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 적절한 오프셋에 메타데이터가 있는 큰 원시 스파스 파일 생성:

`e2image -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 일반 또는 원시 이미지 파일 대신 QCOW2 이미지 파일 생성:

`e2image -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>
