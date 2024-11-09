---
layout: page
title: linux/ark (한국어)
description: "KDE의 압축 도구."
content_hash: 8b31abb26d2fb0c0f30ad353527b995e33057bae
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/ark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ark

KDE의 압축 도구.
더 많은 정보: <https://docs.kde.org/stable5/en/ark/ark/>.

- 특정 압축 파일을 현재 디렉토리에 추출:

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일</span>

- 압축 파일을 특정 디렉토리에 추출:

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일</span>

- 압축 파일이 존재하지 않을 경우 생성하고 특정 파일 추가:

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
