---
layout: page
title: common/ln (한국어)
description: "파일 및 디렉터리에 대한 링크를 생성합니다."
content_hash: ee3bb1e66a9542475fcccab453978f58364d6d63
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ln.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ln

파일 및 디렉터리에 대한 링크를 생성합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- 파일이나 디렉터리에 대한 심볼릭 링크 생성:

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/심볼릭링크</span>

- 다른 파일을 가리키도록 기존 심볼릭 링크를 덮어쓰기:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/새로운_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/심볼릭링크</span>

- 파일에 대한 하드 링크 생성:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/하드링크</span>
