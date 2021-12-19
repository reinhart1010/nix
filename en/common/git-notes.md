---
layout: page
title: common/git-notes (English)
description: "Add or inspect object notes."
content_hash: 1b9801f28576d1bc15e971b6af4a885013b4134c
related_topics:
  - title: français version
    url: /fr/common/git-notes.html
    icon: bi bi-globe
---
# git notes

Add or inspect object notes.
More information: <https://git-scm.com/docs/git-notes>.

- List all notes and the objects they are attached to:

`git notes list`

- List all notes attached to a given object (defaults to HEAD):

`git notes list [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>`]`

- Show the notes attached to a given object (defaults to HEAD):

`git notes show [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>`]`

- Append a note to a specified object (opens the default text editor):

`git notes append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>

- Append a note to a specified object, specifying the message:

`git notes append --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message_text</span>`"`

- Edit an existing note (defaults to HEAD):

`git notes edit [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>`]`

- Copy a note from one object to another:

`git notes copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_object</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_object</span>

- Remove all the notes added to a specified object:

`git notes remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>
