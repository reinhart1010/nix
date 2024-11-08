---
layout: page
title: common/lsyncd (한국어)
description: "파일과 디렉토리를 감시하고 변경 시 `rsync`를 실행."
content_hash: beab415c1d6e746e477923d70010c7c810da8556
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lsyncd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsyncd

파일과 디렉토리를 감시하고 변경 시 `rsync`를 실행.
주로 두 시스템의 디렉토리를 동기화하여 한 디렉토리에서 발생한 변경 사항을 즉시 다른 디렉토리에 반영하기 위해 사용.
더 많은 정보: <https://github.com/lsyncd/lsyncd>.

- 소스를 감시하고 변경 시마다 `rsync`를 실행하여 파일을 대상에 동기화:

`lsyncd -rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트::공유_이름</span>

- `rsyncd` 공유 대신 SSH 사용:

`lsyncd -rsyncssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상</span>
