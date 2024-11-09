---
layout: page
title: linux/compsize (한국어)
description: "btrfs 파일 시스템에서 파일 집합의 압축 비율을 계산합니다."
content_hash: e06e69ccf944b21111a5358498d79165a06f4591
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/compsize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compsize

btrfs 파일 시스템에서 파일 집합의 압축 비율을 계산합니다.
파일을 다시 압축하기 위해 단편화를 해제하는 방법은 `btrfs filesystem`을 참조하세요.
더 많은 정보: <https://github.com/kilobyte/compsize>.

- 파일 또는 디렉터리에 대한 현재 압축 비율 계산:

`sudo compsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 파일 시스템 경계를 넘지 않도록 설정:

`sudo compsize --one-file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 사람이 읽을 수 있는 크기 대신 원시 바이트 수를 표시:

`sudo compsize --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
