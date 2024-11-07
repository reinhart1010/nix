---
layout: page
title: common/rekor-cli (한국어)
description: "소프트웨어 프로젝트의 공급망 내에서 생성된 메타데이터의 변경 불가능한 변조 방지 원장."
content_hash: 46caf2df106f40e61dfb6f1a7dcb27c96cb63f22
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rekor-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rekor-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rekor-cli

소프트웨어 프로젝트의 공급망 내에서 생성된 메타데이터의 변경 불가능한 변조 방지 원장.
더 많은 정보: <https://github.com/sigstore/rekor>.

- 아티팩트를 Rekor에 업로드:

`rekor-cli upload --artifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ext</span>` --signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ext.sig</span>` --pki-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x509</span>` --public-key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.pub</span>

- 투명성 로그의 항목에 대한 정보 얻기:

`rekor-cli get --uuid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1</span>

- 아티팩트로 Rekor 색인에서 항목 검색:

`rekor-cli search --artifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ext</span>

- 특정 해시로 Rekor 색인에서 항목 검색:

`rekor-cli search --sha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b</span>
