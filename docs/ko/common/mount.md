---
layout: page
title: common/mount (한국어)
description: "하나의 폴더에 있는 전체 파일 시스템에 대한 접근을 제공합니다."
content_hash: a27bbe281dc085d0034c55e85b59ff7a67b7274c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/mount.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mount.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount

하나의 폴더에 있는 전체 파일 시스템에 대한 접근을 제공합니다.
더 많은 정보: <https://manned.org/mount.8>.

- 마운트된 모든 파일 시스템 표시:

`mount`

- 폴더에 장치 마운트:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템_종류</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 존재하지 않을 때 특정 폴더를 생성하고, 해당 폴더에 장치를 마운트:

`mount --mkdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 특정 사용자의 폴더에 장치 마운트:

`mount -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_아이디</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- CD-ROM 장치(파일형식 ISO9660)를 `/cdrom` (읽기 전용)에 마운트:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` -o ro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cdrom</span>

- `/etc/fstab`에 정의된 모든 파일 시스템을 마운트:

`mount -a`

- `/etc/fstab`에 설정된 특정 파일 시스템을 마운트 (예, `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my_drive</span>

- 폴더를 다른 폴더에 마운트:

`mount --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이전_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_디렉터리</span>
