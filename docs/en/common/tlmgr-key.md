---
layout: page
title: common/tlmgr-key (English)
description: "Manage GPG keys used to verify TeX Live databases."
content_hash: bdb27017c521c9665ea54de83150674c9d82437f
last_modified_at: 2022-12-04
---
# tlmgr key

Manage GPG keys used to verify TeX Live databases.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all keys for TeX Live:

`tlmgr key list`

- Add a key from a specific file:

`sudo tlmgr key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.gpg</span>

- Add a key from `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.gpg</span>` | sudo tlmgr key add -`

- Remove a specific key by its ID:

`sudo tlmgr key remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>
