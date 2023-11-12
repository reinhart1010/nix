---
layout: page
title: common/enscript (English)
description: "Convert text files to PostScript, HTML, RTF, ANSI, and overstrikes."
content_hash: 1588a25f5b5ebdd7b8cacc89463137fda6a4f4e3
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/enscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# enscript

Convert text files to PostScript, HTML, RTF, ANSI, and overstrikes.
More information: <https://www.gnu.org/software/enscript>.

- Generate a PostScript file from a text file:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Generate a file in a different language than PostScript:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --language=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|rtf|...</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Generate a PostScript file with a landscape layout, splitting the page into columns (maximum 9):

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --columns=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>` --landscape --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Display available syntax highlighting languages and file formats:

`enscript --help-highlight`

- Generate a PostScript file with syntax highlighting and color for a specified language:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --color=1 --highlight=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>
