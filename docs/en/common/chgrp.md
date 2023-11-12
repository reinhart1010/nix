---
layout: page
title: common/chgrp (English)
description: "Change group ownership of files and directories."
content_hash: 9ba75f415fb63f360c02eddbff149961614ed20c
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/chgrp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chgrp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chgrp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chgrp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chgrp

Change group ownership of files and directories.
More information: <https://www.gnu.org/software/coreutils/chgrp>.

- Change the owner group of a file/directory:

`chgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Recursively change the owner group of a directory and its contents:

`chgrp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Change the owner group of a symbolic link:

`chgrp -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- Change the owner group of a file/directory to match a reference file:

`chgrp --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
