---
layout: page
title: linux/qmake (English)
description: "Generate Makefiles from Qt project files."
content_hash: 41724fe84ddf800406e35b78f192feed219dabb2
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/qmake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmake

Generate Makefiles from Qt project files.
More information: <https://doc.qt.io/qt-6/qmake-manual.html>.

- Generate a `Makefile` from a project file in the current directory:

`qmake`

- Specify `Makefile` and project file locations:

`qmake -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Makefile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file.pro</span>

- Generate a default project file:

`qmake -project`

- Compile a project:

`qmake && make`

- Enable debug mode:

`qmake -d`
