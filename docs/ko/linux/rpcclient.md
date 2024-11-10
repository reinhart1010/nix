---
layout: page
title: linux/rpcclient (한국어)
description: "MS-RPC 클라이언트 도구 (samba 모음의 일부)."
content_hash: 548584bd95f3c1ec153cd2734373eff020921b51
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rpcclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpcclient

MS-RPC 클라이언트 도구 (samba 모음의 일부).
더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- 원격 호스트에 연결:

`rpcclient --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`%`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 비밀번호 없이 도메인에 있는 원격 호스트에 연결:

`rpcclient --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --workgroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` --no-pass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 비밀번호 해시를 전달하여 원격 호스트에 연결:

`rpcclient --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --pw-nt-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 원격 호스트에서 셸 명령 실행:

`rpcclient --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`%`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세미콜론_구분_명령들</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 도메인 사용자 표시:

`rpcclient $> enumdomusers`

- 권한 표시:

`rpcclient $> enumprivs`

- 특정 사용자에 대한 정보 표시:

`rpcclient $> queryuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|RID</span>

- 도메인에 새 사용자 생성:

`rpcclient $> createdomuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
