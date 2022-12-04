---
layout: page
title: common/babel (English)
description: "A transpiler which converts code from JavaScript ES6/ES7 syntax to ES5 syntax."
content_hash: ff39569eaeb0f7bd6083548a6df117d06b58e3db
last_modified_at: 2022-12-04
related_topics:
  - title: français version
    url: /fr/common/babel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/babel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/babel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/babel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/babel.html
    icon: bi bi-globe
---
# babel

A transpiler which converts code from JavaScript ES6/ES7 syntax to ES5 syntax.
More information: <https://babeljs.io/>.

- Transpile a specified input file and output to `stdout`:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Transpile a specified input file and output to a specific file:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Transpile the input file every time it is changed:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --watch`

- Transpile a whole directory of files:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>

- Ignore specified comma-separated files in a directory:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignored_files</span>

- Transpile and output as minified JavaScript:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --minified`

- Choose a set of presets for output formatting:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">presets</span>

- Output all available options:

`babel --help`
