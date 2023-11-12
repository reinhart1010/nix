---
layout: page
title: common/mv (English)
description: "Move or rename files and directories."
content_hash: 82306a4773ddb9b60784778e19feea31ac5a3935
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mv

Move or rename files and directories.
More information: <https://www.gnu.org/software/coreutils/mv>.

- Rename a file or directory when the target is not an existing directory:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Move a file or directory into an existing directory:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/existing_directory</span>

- Move multiple files into an existing directory, keeping the filenames unchanged:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source1 path/to/source2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/existing_directory</span>

- Do not prompt for confirmation before overwriting existing files:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Do not overwrite existing files at the target:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Move files in verbose mode, showing files after they are moved:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>
