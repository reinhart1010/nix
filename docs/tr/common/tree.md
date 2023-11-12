---
layout: page
title: common/tree (Türkçe)
description: "Mevcut dizinin içeriğini ağaç biçiminde göster."
content_hash: 7f4a7274b383b98d08f22178337252d91009f7bb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tree

Mevcut dizinin içeriğini ağaç biçiminde göster.
Daha fazla bilgi için: <http://mama.indstate.edu/users/ice/tree/>.

- Dosya ve dizinleri `num` değeri kadar derinlikte göster (1 olması durumunda mevcut dizin gösterilir):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Yalnızca dizinleri göster:

`tree -d`

- Renklendirme açık olacak şekilde gizli dosyaları dahi göster:

`tree -a -C`

- Ağacın satırlarını girintiler yerine tüm yolu belirterek göster:

`tree -i -f`

- Tüm dosyaların ve dizinlerin eklenerek artan boyutlarını, insanların okuyabileceği bir biçimde göster:

`tree -s -h --du`

- Ağaç hiyerarşisi içindeki dosyaları bir wildcard (glob) kalıbı kullanarak ve aranan özellikteki dosyalara sahip olmayan dizinleri yoksayarak göster:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- Ağaç hiyerarşisi içindeki dizinleri bir wildcard (glob) kalıbı kullanarak ve istenen dizine atalığı olmayan dizinleri yoksayarak göster:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin_ismi</span>` --matchdirs --prune`

- Ağacı belirtilen dizinleri yoksayarak göster:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin_ismi1|dizin_ismi2</span>`'`
