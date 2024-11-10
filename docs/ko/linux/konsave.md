---
layout: page
title: linux/konsave (한국어)
description: "한 번의 명령으로 Linux 사용자 설정을 저장하고 적용."
content_hash: 42153065700390b252bad15281d147c2d6f7698f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/konsave.html
    icon: bi bi-globe
tldri18n_status: 2
---
# konsave

한 번의 명령으로 Linux 사용자 설정을 저장하고 적용.
더 많은 정보: <https://github.com/Prayag2/konsave>.

- 현재 설정을 프로필로 저장:

`konsave --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 프로필 적용:

`konsave --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 현재 설정을 프로필로 저장하며, 동일한 이름의 기존 프로필이 있을 경우 덮어쓰기:

`konsave -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` --force`

- 모든 프로필 나열:

`konsave --list`

- 프로필 제거:

`konsave --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 프로필을 `.knsv`로 내보내기하여 홈 디렉토리에 저장:

`konsave --export-profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- `.knsv` 프로필 가져오기:

`konsave --import-profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로필_이름.knsv</span>
