---
layout: page
title: osx/csshx (한국어)
description: "macOS용 클러스터 SSH 도구."
content_hash: d1bab6b442e110a8ba543ad573fb74a4dda12593
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/csshx.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/csshx.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/csshx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csshX

macOS용 클러스터 SSH 도구.
더 많은 정보: <https://github.com/brockgr/csshx>.

- 여러 호스트에 연결:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명2</span>

- 지정된 SSH 키를 사용하여 여러 호스트에 연결:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자@호스트명1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자@호스트명2</span>` --ssh_args "-i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일.pem</span>`"`

- `/etc/clusters`에 정의된 클러스터에 연결:

`csshX cluster1`
