---
layout: page
title: common/smbmap (한국어)
description: "사용자가 전체 도메인에 걸쳐 Samba 공유 드라이브를 열거할 수 있게 합니다."
content_hash: 06419f43cc5d4e26f0058ef1936ed3e11d2b7009
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/smbmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# smbmap

사용자가 전체 도메인에 걸쳐 Samba 공유 드라이브를 열거할 수 있게 합니다.
더 많은 정보: <https://github.com/ShawnDEvans/smbmap>.

- NULL 세션이 활성화되고 공유가 열린 호스트 열거:

`smbmap --host-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 호스트를 열거하고 SMB 파일 권한 확인:

`smbmap --host-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -q`

- 사용자 이름과 비밀번호를 사용하여 IP 또는 호스트 이름에 SMB로 연결:

`smbmap -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_또는_호스트_이름</span>

- 파일 이름 패턴(정규 표현식)으로 검색하고 특정 공유를 제외하면서 N 단계 깊이까지 재귀적으로 파일을 찾아 다운로드:

`smbmap --host-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -q -R --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공유이름</span>` -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일패턴</span>

- 사용자 이름과 비밀번호를 사용하여 SMB를 통해 파일 업로드:

`smbmap -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_또는_호스트_이름</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/공유_이름/원격_파일명</span>`'`
