---
layout: page
title: linux/scrontab (한국어)
description: "Slurm 크론탭 파일을 관리합니다."
content_hash: 141a264cb70233f8d4df091c25b1c904828c8efc
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/scrontab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scrontab

Slurm 크론탭 파일을 관리합니다.
더 많은 정보: <https://slurm.schedmd.com/scrontab.html>.

- 지정된 파일에서 새 크론탭 설치:

`scrontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 현재 사용자의 크론탭 [e]편집:

`scrontab -e`

- 지정된 사용자의 크론탭 [e]편집:

`scrontab --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_ID</span>` -e`

- 현재 크론탭 [r]제거:

`scrontab -r`

- 현재 사용자의 크론탭을 `stdout`에 출력:

`scrontab -l`
