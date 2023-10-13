---
layout: page
title: linux/systemd-creds (English)
description: "List, show, encrypt and decrypt service credentials."
content_hash: 6c7aa66cc05638a07233168411911c2db5da1ffa
last_modified_at: 2023-10-13
---
# systemd-creds

List, show, encrypt and decrypt service credentials.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-creds.html>.

- Encrypt a file and set a specific name:

`systemd-creds encrypt --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Decrypt the file again:

`systemd-creds decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Encrypt text from `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` | systemd-creds encrypt --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Encrypt the text and append it to the service file (the credentials will be available in `$CREDENTIALS_DIRECTORY`):

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` | systemd-creds encrypt --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --pretty - - >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Create a credential that is only valid until the given timestamp:

`systemd-creds encrypt --not-after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timestamp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>
