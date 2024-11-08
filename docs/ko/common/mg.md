---
layout: page
title: common/mg (한국어)
description: "작고 빠르며 이식성이 뛰어난 `emacs` 기반 텍스트 편집기."
content_hash: cc5b68cf0832dbf1f029988c21a6014457226e48
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mg

작고 빠르며 이식성이 뛰어난 `emacs` 기반 텍스트 편집기.
더 많은 정보: <https://github.com/hboetes/mg>.

- 파일을 열어 편집:

`mg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 줄 번호에서 파일 열기:

`mg +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 읽기 전용 모드로 파일 열기:

`mg -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 편집 시 `~` 백업 파일 비활성화:

`mg -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
