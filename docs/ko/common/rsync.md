---
layout: page
title: common/rsync (한국어)
description: "기본적으로 SSH를 사용하여 원격 호스트 간에 파일을 전송합니다(두 원격 호스트 사이는 아닙니다)."
content_hash: 34524b3aedb1ad7459edba0c66c62b6fa71a7e22
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rsync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rsync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rsync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rsync.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rsync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rsync

기본적으로 SSH를 사용하여 원격 호스트 간에 파일을 전송합니다(두 원격 호스트 사이는 아닙니다).
원격 경로를 지정하려면, `호스트:경로/대상/파일_또는_폴더`를 사용하세요.
더 많은 정보: <https://download.samba.org/pub/rsync/rsync.1>.

- 파일 전송:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 아카이브 모드 (디렉토리를 반복적으로 복사하고, 권한, 소유권, 수정 시간을 확인 및 보존하지 않고 심볼릭 링크를 복사) 사용:

`rsync --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 데이터가 대상으로 전송될 때 압축하고, 사람이 읽을 수 있는 자세한 진행 상황을 표시하고, 중단된 경우 부분적으로 전송된 파일 유지:

`rsync --compress --verbose --human-readable --partial --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 반복적으로 폴더 복사:

`rsync --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 디렉터리 내용을 전송하지만, 디렉터리 자체는 전송하지 않음:

`rsync --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 디렉토리를 반복적으로 복사하고, 아카이브 모드를 사용하고, 심볼릭 링크를 확인하고, 대상에 있는 최신 파일을 건너뜀:

`rsync --recursive --archive --update --copy-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- `rsyncd`를 실행하는 원격 호스트로 폴더를 전송하고 소스에 존재하지 않는 대상의 파일으 삭제:

`rsync --recursive --delete rsync://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 기본값(22)이 아닌 다른 포트를 사용하여 SSH를 통해 파일을 전송하고 전체적인 진행 상황을 표시:

`rsync --rsh 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>
