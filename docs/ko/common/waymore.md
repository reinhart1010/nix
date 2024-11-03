---
layout: page
title: common/waymore (한국어)
description: "Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, VirusTotal에서 도메인의 URL을 가져오기."
content_hash: c2d664cc6760cab34c218fc632833e264165796d
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/waymore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/waymore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# waymore

Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, VirusTotal에서 도메인의 URL을 가져오기.
참고: 별도로 지정하지 않으면 출력은 waymore의 `config.yml`이 있는 `results/` 디렉토리에 저장됩니다 (기본적으로 `~/.config/waymore/`).
더 많은 정보: <https://github.com/xnl-h4ck3r/waymore>.

- 도메인의 URL 검색 (출력은 일반적으로 `~/.config/waymore/results/`에 저장됨):

`waymore -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 검색 결과를 도메인의 URL 목록으로만 제한하고 지정된 파일에 출력 저장:

`waymore -mode U -oU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.com-주소.txt</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- URL의 콘텐츠 본문만 출력하고 지정된 디렉토리에 출력 저장:

`waymore -mode R -oR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.com-주소-응답</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 날짜 범위를 지정하여 결과 필터링:

`waymore -from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDD|YYYYMM|YYYY</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDD|YYYYMM|YYYY</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
