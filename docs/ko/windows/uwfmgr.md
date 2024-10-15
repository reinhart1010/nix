---
layout: page
title: windows/uwfmgr (한국어)
description: "통합 쓰기 필터 (UWF)."
content_hash: 5b0dfb55107fd3de9e03740fd10f7bc36e2c1289
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/windows/uwfmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uwfmgr

통합 쓰기 필터 (UWF).
드라이브를 보호하기 위해 드라이브에 대한 모든 쓰기를 가상 오버레이로 리디렉션합니다. 기본적으로 재부팅 후 쓰기는 커밋되지 않으면 삭제됩니다.
더 많은 정보: <https://learn.microsoft.com/windows/iot/iot-enterprise/customize/unified-write-filter>.

- 현재 상태 가져오기:

`uwfmgr get-config`

- 드라이브를 보호로 설정:

`uwfmgr volume protect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이브_문자</span>`:`

- 보호 목록에서 드라이브 제거:

`uwfmgr volume unprotect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이브_문자</span>`:`

- 보호 사용 또는 사용 안 함 (재부팅 후 적용):

`uwfmgr filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- 보호된 드라이브의 파일 변경 사항 커밋:

`uwfmgr file commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이브_문자:\경로\대상\파일</span>

- 보호된 드라이브의 파일 삭제 커밋:

`uwfmgr file commit-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이브_문자:\경로\대상\파일</span>
