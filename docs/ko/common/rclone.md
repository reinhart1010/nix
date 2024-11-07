---
layout: page
title: common/rclone (한국어)
description: "여러 클라우드 서비스와 파일 및 디렉터리를 복사, 동기화 또는 이동."
content_hash: a5fd43e4a97285409a2cca5293dfc91a4f25d77e
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rclone.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rclone.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rclone

여러 클라우드 서비스와 파일 및 디렉터리를 복사, 동기화 또는 이동.
더 많은 정보: <https://rclone.org>.

- rclone 설정을 위한 인터랙티브 메뉴 실행:

`rclone config`

- rclone 원격의 디렉터리 내용 나열:

`rclone lsf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 로컬 머신에서 원격 대상으로 파일이나 디렉터리 복사:

`rclone copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 지난 24시간 내에 변경된 파일들을 사용자 확인을 거쳐 로컬 머신에서 원격으로 복사:

`rclone copy --interactive --max-age 24h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_폴더</span>

- 특정 파일이나 디렉터리 미러링 (참고: 복사와 달리, 동기화는 로컬에 존재하지 않는 파일을 원격에서 제거):

`rclone sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 원격 파일이나 디렉터리 삭제 (참고: `--dry-run`은 테스트를 의미하며, 실제로 삭제하려면 명령에서 제거):

`rclone --dry-run delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- rclone 원격 마운트 (실험적):

`rclone mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- CTRL-C 실패 시 rclone 원격 마운트 해제 (실험적):

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>
