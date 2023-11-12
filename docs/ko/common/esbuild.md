---
layout: page
title: common/esbuild (한국어)
description: "속도를 위해 제작된 자바스크립트 번들러 및 압축 도구."
content_hash: 00997acd42e62f5903dd0a4ff5427901c03b1807
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/esbuild.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/esbuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# esbuild

속도를 위해 제작된 자바스크립트 번들러 및 압축 도구.
더 많은 정보: <https://esbuild.github.io/>.

- 자바스크립트 애플리케이션을 번들로 묶어 `stdout`으로 인쇄:

`esbuild --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- `stdin`에서 JSX 애플리케이션 번들링:

`esbuild --bundle --outfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jsx</span>

- `production` 모드에서 소스맵을 사용하여 JSX 애플리케이션을 번들로 묶고 압축:

`esbuild --bundle --define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.env.NODE_ENV=\"production\"</span>` --minify --sourcemap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- 쉼표로 구분된 브라우저 목록을 위해 JSX 애플리케이션을 번들로 묶음:

`esbuild --bundle --minify --sourcemap --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chrome58,firefox57,safari11,edge16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jsx</span>

- 특정 노드 버전에 대한 자바스크립트 애플리케이션 번들:

`esbuild --bundle --platform=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>` --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- `.js` 파일에 JSX 구문을 활성화하는 자바스크립트 애플리케이션을 번들로 묶음:

`esbuild --bundle app.js --loader:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.js=jsx</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- HTTP 서버에서 자바스크립트 애플리케이션을 번들링하고 제공:

`esbuild --bundle --serve=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --outfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- 파일 목록을 출력 폴더에 번들링:

`esbuild --bundle --outdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
