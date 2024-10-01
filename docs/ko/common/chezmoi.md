---
layout: page
title: common/chezmoi (한국어)
description: "Go로 작성된, 다중 머신 도트파일 관리자."
content_hash: 7b22b56855aeb4210799f6ac3b655fbc349f05a7
last_modified_at: 2024-10-01
related_topics:
  - title: English version
    url: /en/common/chezmoi.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chezmoi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Chezmoi

Go로 작성된, 다중 머신 도트파일 관리자.
참고: `stow`, `tuckr`, `vcsh`, `homeshick`.
더 많은 정보: <https://chezmoi.io>.

- `chezmoi`를 설정하고, `~/.local/share/chezmoi`에 Git 저장소를 만듬:

`chezmoi init`

- Git 저장소의 기존 도트 파일에서 `chezmoi`를 설정:

`chezmoi init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- 하나 이상의 도트 파일 추적을 시작:

`chezmoi add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도트파일1 경로/대상/도트파일2 ...</span>

- 로컬 변경 사항으로 저장소 업데이트:

`chezmoi re-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도트파일1 경로/대상/도트파일2 ...</span>

- 추적된 도트파일의 소스 상태를 편집:

`chezmoi edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도트파일_또는_심볼릭링크</span>

- 대기 중인 변경사항 보기:

`chezmoi diff`

- 변경 사항을 적용:

`chezmoi -v apply`

- 원격 저장소에서 변경 사항을 가져와 적용:

`chezmoi update`
