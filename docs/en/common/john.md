---
layout: page
title: common/john (English)
description: "Password cracker."
content_hash: e70c177bfe1242f4d35c45cd39f14b3c4d3c5dd5
last_modified_at: 2024-01-31
related_topics:
  - title: français version
    url: /fr/common/john.html
    icon: bi bi-globe
tldri18n_status: 2
---
# john

Password cracker.
More information: <https://www.openwall.com/john/>.

- Crack password hashes:

`john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- Show passwords cracked:

`john --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- Display users' cracked passwords by user identifier from multiple files:

`john --show --users=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_ids</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes1.txt path/to/hashes2.txt ...</span>

- Crack password hashes, using a custom wordlist:

`john --wordlist=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- List available hash formats:

`john --list=formats`

- Crack password hashes, using a specific hash format:

`john --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5crypt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- Crack password hashes, enabling word mangling rules:

`john --rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- Restore an interrupted cracking session from a state file, e.g. `mycrack.rec`:

`john --restore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mycrack.rec</span>
