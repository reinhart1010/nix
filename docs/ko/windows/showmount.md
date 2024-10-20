---
layout: page
title: windows/showmount (한국어)
description: "NFS 파일 시스템에 대한 정보를 표시합니다."
content_hash: 534ae87d2411e84c8935a0494fd5c5589e910790
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/showmount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# showmount

NFS 파일 시스템에 대한 정보를 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- 내보낸 모든 파일 시스템을 표시:

`showmount -e`

- 모든 NFS 클라이언트와 마운트된 디렉터리를 표시:

`showmount -a`

- NFS로 마운트된 모든 디렉터리 표시:

`showmount -d`

- 원격 서버에 대해 내보낸 모든 파일 시스템을 표시:

`showmount -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_주소</span>
