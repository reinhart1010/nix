---
layout: page
title: common/esbuild (English)
description: "JavaScript bundler and minifier built for speed."
content_hash: d46499ed5fe1ea11f599f9ad9cbbaa08754dc7ba
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/esbuild.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/esbuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# esbuild

JavaScript bundler and minifier built for speed.
More information: <https://esbuild.github.io/>.

- Bundle a JavaScript application and print to `stdout`:

`esbuild --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle a JSX application from `stdin`:

`esbuild --bundle --outfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out.js</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jsx</span>

- Bundle and minify a JSX application with source maps in `production` mode:

`esbuild --bundle --define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.env.NODE_ENV=\"production\"</span>` --minify --sourcemap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle a JSX application for a comma-separated list of browsers:

`esbuild --bundle --minify --sourcemap --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chrome58,firefox57,safari11,edge16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jsx</span>

- Bundle a JavaScript application for a specific node version:

`esbuild --bundle --platform=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>` --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle a JavaScript application enabling JSX syntax in `.js` files:

`esbuild --bundle app.js --loader:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.js=jsx</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle and serve a JavaScript application on an HTTP server:

`esbuild --bundle --serve=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --outfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle a list of files to an output directory:

`esbuild --bundle --outdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
