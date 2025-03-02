---
layout: page
title: windows/cipher (한국어)
description: "NTFS 볼륨에서 디렉터리와 파일의 암호화를 표시하거나 변경."
content_hash: abc10d11128c6015c2a3c3f75469443199b7f7c1
last_modified_at: 2024-11-06
related_topics:
  - title: Deutsch version
    url: /de/windows/cipher.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cipher.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cipher.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cipher.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cipher

NTFS 볼륨에서 디렉터리와 파일의 암호화를 표시하거나 변경.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- 특정 암호화된 파일 또는 디렉터리에 대한 정보 표시:

`cipher /c:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉터리</span>

- 파일 또는 디렉터리를 [e]암호화 (디렉터리가 표시되므로 이후에 추가된 파일도 암호화됨):

`cipher /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉터리</span>

- 파일 또는 디렉터리 [d]암호 해독:

`cipher /d:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉터리</span>

- 파일 또는 디렉터리를 안전하게 제거:

`cipher /w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉터리</span>
