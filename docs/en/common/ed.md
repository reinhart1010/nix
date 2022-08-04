---
layout: page
title: common/ed (English)
description: "The original Unix text editor."
content_hash: bf6f45f4a40d7e637c31c619148fb8f638f2f7c7
related_topics:
  - title: italiano version
    url: /it/common/ed.html
    icon: bi bi-globe
---
# ed

The original Unix text editor.
More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start ed, editing an empty document (which can be saved as a new file in the current directory):

`ed`

- Start ed, editing an empty document, with `:` as a command prompt indicator:

`ed -p :`

- Start ed editing an existing file (this shows the byte count of the loaded file):

`ed -p : `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Toggle the printing of error explanations. (By default, explanations are not printed and only a `?` appears):

`H`

- Add text to the current document. Mark completion by entering a period by itself in a new line:

`a<Enter>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text_to_insert</span>`<Enter>.`

- Print the entire document (`,` is a shortcut to the range `1,$` which covers the start to the end of the document):

`,p`

- Write the current document to a new file (the filename can be omitted if `ed` was called with an existing file):

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Quit ed:

`q`
