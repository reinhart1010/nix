---
layout: page
title: common/nbtscan (한국어)
description: "네트워크를 스캔하여 NetBIOS 이름 정보를 검색."
content_hash: e1efb5f1bffcf59c61fa8e56b6dff0e3486b46a7
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nbtscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nbtscan

네트워크를 스캔하여 NetBIOS 이름 정보를 검색.
더 많은 정보: <https://github.com/resurrecting-open-source-projects/nbtscan>.

- 네트워크에서 NetBIOS 이름 스캔:

`nbtscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- 단일 IP 주소 스캔:

`nbtscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>

- 자세한 출력 표시:

`nbtscan -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- `/etc/hosts` 형식으로 출력 표시:

`nbtscan -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- 스캔할 IP 주소/네트워크를 파일에서 읽기:

`nbtscan -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>
