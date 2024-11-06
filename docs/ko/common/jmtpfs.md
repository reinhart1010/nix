---
layout: page
title: common/jmtpfs (한국어)
description: "MTP 장치에 액세스하기 위한 FUSE 기반 파일 시스템."
content_hash: db20f6e2396c048ffc5c53fff74e925966064ead
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jmtpfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jmtpfs

MTP 장치에 액세스하기 위한 FUSE 기반 파일 시스템.
더 많은 정보: <https://manned.org/jmtpfs>.

- MTP 장치를 디렉토리에 마운트:

`jmtpfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 마운트 옵션 설정:

`jmtpfs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">allow_other,auto_unmount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사용 가능한 MTP 장치 나열:

`jmtpfs --listDevices`

- 여러 장치가 있는 경우 특정 장치 마운트:

`jmtpfs -device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스_ID</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- MTP 장치 마운트 해제:

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
