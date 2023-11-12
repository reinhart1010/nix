---
layout: page
title: common/rm (한국어)
description: "파일 혹은 폴더를 삭제."
content_hash: 71cd4e3df0e5de9452e10b44d92fb135cd361320
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

파일 혹은 폴더를 삭제.
더 많은 정보: <https://www.gnu.org/software/coreutils/rm>.

- 임의의 경로에서 파일을 제거:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일의/경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다른/파일의/경로</span>

- 재귀적으로 폴더와 그 폴더내의 하위폴더들을 모두 제거:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더의/경로</span>

- 강제로 폴더를 제거, 확인절차와 에러메시지를 띄우지 않음:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더의/경로</span>

- 여라개의 파일을 하나씩 확인받으면서 제거:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일들</span>

- 상세화면과 함께 파일을 제거, 삭제된 파일에 대해 메시지를 출력함:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더의/경로/*</span>
