---
layout: page
title: linux/mount.cifs (한국어)
description: "SMB (Server Message Block) 또는 CIFS (Common Internet File System) 공유를 마운트."
content_hash: 8c5e3933737868609c04bdbd217c794e5754a3b0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mount.cifs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mount.cifs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount.cifs

SMB (Server Message Block) 또는 CIFS (Common Internet File System) 공유를 마운트.
참고: `mount`에 `-t cifs` 옵션을 전달하여 동일한 작업을 수행할 수 있습니다.
더 많은 정보: <https://manned.org/mount.cifs>.

- 지정된 사용자명 또는 기본적으로 `$USER`를 사용하여 연결 (비밀번호 입력 필요):

`mount.cifs -o user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공유_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>

- 게스트 사용자로 연결 (비밀번호 없이):

`mount.cifs -o guest //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공유_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>

- 마운트된 디렉토리의 소유권 정보 설정:

`mount.cifs -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_ID|사용자명</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_ID|그룹명</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공유_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>
