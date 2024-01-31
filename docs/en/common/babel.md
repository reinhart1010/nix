---
layout: page
title: common/babel (English)
description: "A transpiler which converts code from JavaScript ES6/ES7 syntax to ES5 syntax."
content_hash: 78d0f644440657d85d0074bfdcd87f0a6a4f938d
last_modified_at: 2024-01-31
related_topics:
  - title: français version
    url: /fr/common/babel.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/babel.html
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
tldri18n_status: 2
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

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignored_file1,ignored_file2,...</span>

- Transpile and output as minified JavaScript:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --minified`

- Choose a set of presets for output formatting:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">preset1,preset2,...</span>

- Display help:

`babel --help`
