# 変更履歴

## V1.3 - 10 May 2021

We are proud to announce the introduction of a new document build pipeline, which is major milestone for our project. The build pipeline is based on [Pandocker](https://github.com/dalibo/pandocker) and [Github Actions](https://github.com/OWASP/owasp-masvs/tree/master/.github/workflows). This significantly reduces the time spent on creating new releases. We would like to thank:

- Jeroen Willemsen for kick-starting this initiative last year!
- Damien Clochard and Dalibo for supporting and professionalizing the build pipeline.

The build pipeline will also be the foundation for the OWASP MSTG and will be made available for the OWASP ASVS project.

The following changes are part of release 1.3:

- 4 more translations are available, which are Hindi, Farsi, Portuguese and Brazilian Portuguese
- Added requirement MSTG-PLATFORM-11

## V1.2 - 2020年3月7日 - 国際公開

The following changes are part of release 1.2:

- Translation in simplified Chinese of the MASVS available.
- Change of title in MASVS book cover.
- Removed Mobile Top 10 and CWE from MSTG and merged to existing references in MASVS.

## V1.2-RC - 2019年10月5日 - プレリリース

次の変更点は、リリース1.2の一部です:

- flagshipステータスに昇格。
- 要件変更: MSTG-STORAGE-1 「使用する必要がある」。
- 要件 MSTG-STORAGE-13, MSTG-STORAGE-14, および MSTG-STORAGE-15 を追加。データ保護にフォーカス。
- 要件 MSTG-AUTH-11 を更新。コンテキスト情報を保持。
- 要件 MSTG-CODE-4 を更新。単なるデバッグ以上をカバー。
- 要件 MSTG-PLATFORM-10 を追加。 WebView をさらに安全に使用。
- 要件 MSTG-AUTH-12 を追加。特にマルチユーザーアプリの場合に、認可が実装されていることを開発者に想起。
- リスク評価を考慮する場合のMASVSの使用方法に関する説明を若干追加。
- 有料コンテンツに関する説明を若干追加。
- 要件 MSTG-ARCH-11 を追加。 L2 アプリケーションに責任ある開示ポリシーを含める。
- 要件 MSTG-ARCH-12 を追加。関連する国際的なプライバシー法に準拠する必要があることをアプリケーション開発者に提示。
- すべての参照に一貫したスタイルを作成。
- 要件 MSTG-PLATFORM-11 を追加。サードパーティキーボードを介したスパイ行為に対抗。
- 要件 MSTG-MSTG-RESILIENCE-13 を追加。アプリケーションでの盗聴を防止。
- MASVS の各言語版を更新: 中国語(繁体字)、英語、ドイツ語、フランス語、ロシア語、スペイン語、日本語。

## V1.1.4 - 2019年6月4日- サミット版

次の変更点は、リリース1.1.4に含まれています:

- Markdownに関わるあらゆる問題を修正
- フランス語とスペイン語の翻訳を更新
- 日本語と中国語(簡体字)版において「変更履歴」を翻訳
- Markdownの検証と文中のURLの到達性を自動テストするよう設定
- それぞれの要件を特定するための「MSTGコード」ラベルを追加。これは、MSTGの将来のバージョンにおいて、推奨事項やテストケースを容易に見つけられるようにするためのものです。
- リポジトリサイズを削減。.gitignoreにGeneratedを追加。
- 行動規範と貢献者向けガイドラインを追加
- プルリクエストテンプレートを追加
- Gitbookウェブサイトをホストするのに用いているレポジトリの同期を更新
- 全翻訳版のXML/JSON/CSV を生成するスクリプトを更新
- 中国語（簡体字）の前書きを翻訳

## V1.1.3 - 2019年1月9日 軽微な修正

次の変更点は、リリース1.1.3に含まれています:

- スペイン語版の要件7.1における翻訳ミスを修正。
- 謝辞において翻訳者を記載。
- 日本語版における翻訳の軽微な修正。

## V1.1.2 - 2019年1月3日 スポンサーシップと国際化

次の変更点は、リリース1.1.2に含まれています:

- e-bookの購入者への感謝を追加
- V4において、認証のリンクが欠落していた部分に追加、また認証の欠如についてのリンクを更新。
- 英語版の4.7と4.8が入れ替わっていた問題を修正
- 国際版初版
  - スペイン語版を修正し、英語版(1.1.2)に追従。
  - ロシア語版を修正し、英語版(1.1.2)に追従。
  - 中国語(繁体字)版、フランス語版、ドイツ語版、日本語版を初めて追加。
  - 翻訳の便宜のため、ドキュメントをシンプルに。
- 自動リリースについてのインストラクションを追加。

## V1.1.0 - 2018年6月14日

次の変更点は、リリース1.1に含まれています::

- 要件 2.6 「機微情報を含んでいる可能性のあるテキストフィールドにおいてクリップボードが無効化されている」を削除。
- 要件 2.2 「機密データはアプリコンテナまたはシステムの資格情報保存機能の外部に保存されていない」を追加。
- 要件 2.1 を「個人識別情報、ユーザー資格情報、暗号化鍵などの機密データを格納するために、システムの資格情報保存機能が適切に使用されている。」と表現を調整。

## V1.0 - 2018年1月12日

次の変更点はリリース1.0に含まれています。

- 8.9は8.12と同様であるため削除
- 4.6を一般的な表現に変更
- 微細な修正 (タイプミスなど)
