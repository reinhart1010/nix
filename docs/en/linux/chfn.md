---
layout: page
title: linux/chfn (English)
description: "Update `finger` info for a user."
content_hash: 254aeeedabf227abb7dc8ecc6cde542d56532587
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# chfn

Update `finger` info for a user.
More information: <https://manned.org/chfn>.

- Update a user's "Name" field in the output of `finger`:

`chfn -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_display_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Update a user's "Office Room Number" field for the output of `finger`:

`chfn -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_office_room_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Update a user's "Office Phone Number" field for the output of `finger`:

`chfn -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_office_telephone_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Update a user's "Home Phone Number" field for the output of `finger`:

`chfn -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_home_telephone_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
