---
layout: page
title: windows/comp (한국어)
description: "두 파일 또는 파일 집합의 내용을 비교."
content_hash: 5b02ba11ea1572067db8279987fe70a4144af3ad
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/comp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/comp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/comp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/comp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comp

두 파일 또는 파일 집합의 내용을 비교.
파일 집합을 비교하려면 와일드카드(*)를 사용.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- 파일을 대화형으로 비교:

`comp`

- 지정된 두 파일 비교:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 두 파일 집합 비교:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더1</span>`\* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더2</span>`\*`

- 차이점을 10진수 형식으로 표시:

`comp /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 차이점을 ASCII 형식으로 표시:

`comp /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 차이점에 대한 줄 번호 표시:

`comp /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 대소문자를 구분하지 않고 파일 비교:

`comp /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 각 파일의 처음 5줄만 비교:

`comp /n=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>
