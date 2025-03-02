---
layout: page
title: common/olevba (English)
description: "Parse OLE and OpenXML files (e.g., DOC, XLS, PPT, etc.) to extract VBA macros, deobfuscate, and analyze malicious code."
content_hash: 9e9724fece677fbe8e208114ee66038226368b36
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/olevba.html
    icon: bi bi-globe
tldri18n_status: 2
---
# olevba

Parse OLE and OpenXML files (e.g., DOC, XLS, PPT, etc.) to extract VBA macros, deobfuscate, and analyze malicious code.
Part of the `python-oletools` suite.
For more information: <https://github.com/decalage2/oletools>.

- Analyze a file, showing both macro code and analysis results:

`olevba `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively analyze all supported files in a directory:

`olevba -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Provide a password for encrypted Microsoft Office files (may be repeated):

`olevba --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/encrypted_file</span>

- Display only analysis results, without showing macro source code:

`olevba -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display only macro source code:

`olevba -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show obfuscated strings and their decoded content:

`olevba --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
