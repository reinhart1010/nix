---
layout: page
title: common/mv (한국어)
description: "파일 및 디렉토리를 이동하거나 이름을 변경합니다."
content_hash: 38310e6c8b5e2fb028980efdfd90de8297747a21
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mv

파일 및 디렉토리를 이동하거나 이름을 변경합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- 대상이 기존 디렉토리가 아닌 경우 파일 또는 디렉토리 이름 변경:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

- 파일 또는 디렉토리를 기존 디렉토리로 이동:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/기존_폴더</span>

- 여러 파일을 기존 디렉토리로 이동하고 파일 이름은 그대로 유지:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본1 경로/대상/원본2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/기존_폴더</span>

- 기존 파일을 덮어쓸 때 확인하지 않고 ([f]) 이동:

`mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟</span>

- 파일 권한과 관계없이 기존 파일을 덮어쓸 때 [i]대화형 확인 요청:

`mv --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟</span>

- 대상에서 기존 파일을 덮어쓰지 않음 ([n]):

`mv --no-clobber `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟</span>

- 파일 이동 후 [v]자세한 모드로 파일 보기:

`mv --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟</span>

- 외부 도구를 사용하여 이동 가능한 파일을 수집하기 위해 [t]타겟 디렉터리 지정:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find /var/log -type f -name '*.log' -print0</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs -0</span>` mv --target-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟_디렉터리</span>
