---
layout: page
title: common/astyle (English)
description: "Source code indenter, formatter, and beautifier for the C, C++, C# and Java programming languages."
content_hash: 02e51112145dd8b256594592f9bde4c3d8658978
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/astyle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/astyle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/astyle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/astyle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# astyle

Source code indenter, formatter, and beautifier for the C, C++, C# and Java programming languages.
Upon running, a copy of the original file is created with an ".orig" appended to the original file name.
More information: <http://astyle.sourceforge.net>.

- Apply the default style of 4 spaces per indent and no formatting changes:

`astyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>

- Apply the Java style with attached braces:

`astyle --style=java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Apply the allman style with broken braces:

`astyle --style=allman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Apply a custom indent using spaces. Choose between 2 and 20 spaces:

`astyle --indent=spaces=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_spaces</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Apply a custom indent using tabs. Choose between 2 and 20 tabs:

`astyle --indent=tab=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_tabs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
