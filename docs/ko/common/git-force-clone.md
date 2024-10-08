---
layout: page
title: common/git-force-clone (한국어)
description: "`git clone`의 기본 기능을 제공하지만, 대상 Git 저장소가 이미 존재하는 경우 원격의 클론으로 강제 리셋합니다."
content_hash: 0f5b127e4c5cfd385f8c661f7bf34e454b53b234
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-force-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git force-clone

`git clone`의 기본 기능을 제공하지만, 대상 Git 저장소가 이미 존재하는 경우 원격의 클론으로 강제 리셋합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- 새로운 디렉토리에 Git 저장소 클론:

`git force-clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 브랜치를 체크아웃하여 새로운 디렉토리에 Git 저장소 클론:

`git force-clone -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 기존 Git 저장소 디렉토리에 Git 저장소 클론, 원격과 유사하게 강제 리셋을 수행하고 특정 브랜치를 체크아웃:

`git force-clone -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
