---
layout: page
title: linux/instaloader (한국어)
description: "Instagram에서 사진, 비디오, 캡션 및 기타 메타데이터를 다운로드."
content_hash: fe7ef5eadbaa1c0a94364db19a10754abbe9ea49
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/instaloader.html
    icon: bi bi-globe
tldri18n_status: 2
---
# instaloader

Instagram에서 사진, 비디오, 캡션 및 기타 메타데이터를 다운로드.
참고: 고품질 미디어 다운로드를 위해 Instagram 로그인 정보가 필요합니다.
더 많은 정보: <https://instaloader.github.io>.

- 프로필 다운로드:

`instaloader `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 하이라이트 다운로드:

`instaloader --highlights `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 지오태그가 포함된 게시물 다운로드 (사용 가능한 경우) 및 사용자 상호작용 억제:

`instaloader --quiet --geotags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- HTTP 요청에 사용할 사용자 에이전트 지정:

`instaloader --user-agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_에이전트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 로그인 정보 지정 및 게시물 다운로드 (비공개 프로필에 유용):

`instaloader --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 처음 다운로드된 파일이 발견되면 대상을 건너뜀 (Instagram 아카이브 업데이트에 유용):

`instaloader --fast-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 스토리 및 IGTV 비디오 다운로드 (로그인 필요):

`instaloader --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --stories --igtv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 모든 유형의 게시물 다운로드 (로그인 필요):

`instaloader --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --stories --igtv --highlights `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>
