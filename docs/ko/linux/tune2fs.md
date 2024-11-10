---
layout: page
title: linux/tune2fs (한국어)
description: "ext2, ext3 또는 ext4 파일 시스템의 매개변수를 조정합니다."
content_hash: 2183757f3faa6494a8b0b9632c347b3c944781bf
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/tune2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tune2fs

ext2, ext3 또는 ext4 파일 시스템의 매개변수를 조정합니다.
마운트된 파일 시스템에서도 사용할 수 있습니다.
더 많은 정보: <https://manned.org/tune2fs>.

- 파일 시스템이 검사되기 전 최대 횟수를 2로 설정:

`tune2fs -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템 레이블을 MY_LABEL로 설정:

`tune2fs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'MY_LABEL'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템에 대해 디스카드 및 사용자 지정 확장 속성을 활성화:

`tune2fs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">discard,user_xattr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템에 저널링 활성화:

`tune2fs -o^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nobarrier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
