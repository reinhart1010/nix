---
layout: page
title: linux/debugfs (한국어)
description: "대화형 ext2/ext3/ext4 파일 시스템 디버거."
content_hash: 6fdd8e98718e09462182aefd420d341165b89eab
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/debugfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debugfs

대화형 ext2/ext3/ext4 파일 시스템 디버거.
더 많은 정보: <https://manned.org/debugfs>.

- 파일 시스템을 읽기 전용 모드로 열기:

`debugfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템을 읽기/쓰기 모드로 열기:

`debugfs -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 지정된 파일에서 명령을 읽어 실행하고 종료:

`debugfs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/명령_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- debugfs 콘솔에서 파일 시스템 통계 보기:

`stats`

- 파일 시스템 닫기:

`close -a`

- 사용 가능한 모든 명령 나열:

`lr`
