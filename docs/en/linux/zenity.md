---
layout: page
title: linux/zenity (English)
description: "Display dialogs from the command-line/shell scripts."
content_hash: 3dc0d69eac9ebbe9edac6bfe0387cce689f5e4d6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zenity

Display dialogs from the command-line/shell scripts.
Return user-inserted values or 1 if error.
More information: <https://manned.org/zenity>.

- Display the default question dialog:

`zenity --question`

- Display an info dialog displaying the text "Hello!":

`zenity --info --text="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello!</span>`"`

- Display a name/password form and output the data separated by ";":

`zenity --forms --add-entry="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name</span>`" --add-password="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Password</span>`" --separator="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`"`

- Display a file selection form in which the user can only select directories:

`zenity --file-selection --directory`

- Display a progress bar which updates its message every second and show a progress percent:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")</span>` | zenity --progress`
