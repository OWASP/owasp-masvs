# 修改日誌

## V1.3 - 11 May 2021

We are proud to announce the introduction of a new document build pipeline, which is major milestone for our project. The build pipeline is based on [Pandocker](https://github.com/dalibo/pandocker) and [Github Actions](https://github.com/OWASP/owasp-masvs/tree/master/.github/workflows). This significantly reduces the time spent on creating new releases. We would like to thank:

- Jeroen Willemsen for kick-starting this initiative last year!
- Damien Clochard and Dalibo for supporting and professionalizing the build pipeline.

The build pipeline will also be the foundation for the OWASP MSTG and will be made available for the OWASP ASVS project.

The following changes are part of release 1.3:

- 4 more translations are available, which are Hindi, Farsi, Portuguese and Brazilian Portuguese
- Added requirement MSTG-PLATFORM-11

## V1.2 - 2020年3月7日-國際發行

The following changes are part of release 1.2:

- Translation in simplified Chinese of the MASVS available.
- Change of title in MASVS book cover.
- Removed Mobile Top 10 and CWE from MSTG and merged to existing references in MASVS.

## V1.2-RC - 2019年10月5号 - 预发行版 (仅限英语)

以下为1.2-RC版本所包含的更新内容：

晋升为同类安全指南最成功的作品。

- 更改要求 MSTG-STORAGE-1 "需要被使用"（need to be used）。
- 增加侧重于数据保护的要求 MSTG-STORAGE-13， MSTG-STORAGE-14， 和 MSTG-STORAGE-15。
- 更新要求MSTG-AUTH-11，以保护上下文信息（contextual information）。
- 更新要求MSTG-CODE-4，以涵盖更多信息而不仅仅是排错调试（debugging）。
- 添加要求MSTG-PLATFORM-10，以进一步安全的使用WebViews。
- 添加要求MSTG-AUTH-12，以提醒开发人员部署授权，特别是在多用户应用程序（multi-user apps）的情况下。
- 在怎样使用MASVS进行风险评估中添加了一点描述。
- 在付费内容（paid content）中添加了一点描述。
- 增加要求MSTG-ARCH-11，以包含针对L2应用程序的 责任披露政策（Responsible Disclosure policy）。
- 增加要求MSTG-ARCH-12，以向应用程序开发人员展示他们应遵守的相关的国际隐私法律。
- 为英文版的引用（references）创建了一个固定的格式。
- 添加要求MSTG-PLATFORM-11，以反击通过第三方键盘进行的间谍活动（spying）。
- 添加要求MSTG-MSTG-RESILIENCE-13，以阻止在应用程序中的窃听。

## V1.1.4 - 2019年7月4日 - 高峰會版本

以下為 1.1.4 版本內所包含的修正資料:

- 修正所有輕量級標記語言問題。
- 更新法文及西班牙文翻譯版。
- 完成繁體中文及日文版本的修改日誌翻譯。
- 將輕量級標記語言句法進行自動化確認並確定所有網址皆可連線。
- 新增標記代碼到各項需求，以利於未來在 MSTG 當中可以快速及方便的找到相關建議及測試方案。
- 縮減倉儲大小，新增 Generated 到 .gitignore。
- 新增行為守則及共做規則。
- 新增拉取要求(Pull Request)模版。
- 更新與 Gitbook 網頁同步倉儲的功能。
- 更新所有翻譯版本產出  XML/JSON/CSV 的執行腳本。
- 完成繁體中文版本前言部分翻譯。

## V1.1.3版 - 2019年1月9日 小幅度修正

以下為 1.1.3 版本內所包含的修正資料:

- 修正需求 7.1 內的西班牙文翻譯。
- 於致謝區重新安排翻譯者名字。
- 日文版小幅度修正。

## V1.1.2 - 2019年1月3日 贊助者與國際翻譯版本

以下為 1.1.2 版本內所包含的修正資料:

- 新增感謝函給予購買電子書版本的使用者。
- 在V4中添加了丟失的身份驗證連接和更新損壞的身份驗證。
- 修正英文版當中 4.7 與 4.8 的互換。
- 第一次的國際翻譯版本!
  - 修正西班牙文翻譯。翻譯目前已與英文版同步（1.1.2)。
  - 修正俄羅斯文翻譯。翻譯目前已與英文版同步（1.1.2)。
  - 新增第一版繁體中文，法文，德文，以及日文翻譯版本！
- 簡化文件格式方便後續翻譯工作。
- 新增自動化發佈的方式。

## V1.1.0 - 2018年7月14日

以下為 1.1 版本內所包含的修正資料:

- 移除需求 2.6 "在可能包含敏感資料的文字欄位上停用剪貼板"。
- 新增需求 2.2 "任何敏感資料不可被儲存在應用程式容器之外或其他系統層的敏感資料儲存系統"。
- 重新修改用詞於需求 2.1 改為 "系統層的敏感資料儲存系統可適當的用於儲存敏感資料，例如個人資料，使用者資料，或是加密金鑰"。

## V1.0 - 2018年1月12日

以下為 1.0 版本內所包含的修正資料:

- 因需求 8.12 與需求 8.9 相同，刪除 8.9。
- 將需求 4.6 修改為較廣義定義。
- 其他小幅度修改 (錯字或文法等)
