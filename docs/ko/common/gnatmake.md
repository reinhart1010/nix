---
layout: page
title: common/gnatmake (한국어)
description: "Ada 프로그램용 저수준 빌드 도구 (GNAT 도구 체인의 일부)."
content_hash: 1b28dfe9c4e27c38a088b65dea9787bdb28a4a57
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gnatmake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnatmake

Ada 프로그램용 저수준 빌드 도구 (GNAT 도구 체인의 일부).
더 많은 정보: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Building-with-gnatmake.html>.

- 실행 파일을 컴파일:

`gnatmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일1.adb 소스_파일2.adb ...</span>

- 사용자 정의 실행 파일 이름을 설정:

`gnatmake -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.adb</span>

- 강제([f]orce) 재컴파일:

`gnatmake -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.adb</span>
