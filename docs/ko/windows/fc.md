---
layout: page
title: windows/fc (한국어)
description: "두 파일 또는 파일 집합 간의 차이점을 비교."
content_hash: df7cd639636edb8b2d9bf8f5624078c9397cda7e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/fc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fc.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/fc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc

두 파일 또는 파일 집합 간의 차이점을 비교.
와일드카드(*)를 사용하여 파일 집합을 비교할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- 지정된 두 파일 비교:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 대소문자를 구분하지 않고 비교:

`fc /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 파일을 유니코드 텍스트로 비교:

`fc /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 파일을 ASCII 텍스트로 비교:

`fc /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 파일을 이진으로 비교:

`fc /b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 탭을 공백으로 확장하지 않음:

`fc /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>

- 비교를 위해 공백(탭 및 공백) 압축:

`fc /w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일2</span>
