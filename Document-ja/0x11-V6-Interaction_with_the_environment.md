# V6: プラットフォーム連携要件

## 管理目標

アプリがセキュアな方法でプラットフォームAPIや標準コンポーネントを使用していることをこのグループのコントロールは確認します。また、コントロールはアプリ間通信(IPC)も扱います。

## セキュリティ検証要件

| # | 説明 | L1 | L2 |
| --- | --- | --- | --- |
| **6.1** | アプリは必要となる最低限のパーミッションのみを要求している。 | ✓ | ✓ |
| **6.2** | 外部ソースおよびユーザーからの入力はすべて検証されており、必要に応じてサニタイズされている。これにはUI、インテントやカスタムURLなどのIPCメカニズム、ネットワークソースを介して受信したデータを含んでいる。 | ✓ | ✓ |
| **6.3** | アプリはメカニズムが適切に保護されていない限り、カスタムURLスキームを介して機密な機能をエクスポートしていない。 | ✓ | ✓ |
| **6.4** | アプリはメカニズムが適切に保護されていない限り、IPC機構を通じて機密な機能をエクスポートしていない。 | ✓ | ✓ |
| **6.5** | 明示的に必要でない限りWebViewでJavaScriptが無効化されている。 | ✓ | ✓ |
| **6.6** | WebViewは最低限必要のプロトコルハンドラのセットのみを許可するよう構成されている（理想的には、httpsのみがサポートされている）。file, tel, app-id などの潜在的に危険なハンドラは無効化されている。 | ✓ | ✓ |
| **6.7** | アプリのネイティブメソッドがWebViewに公開されている場合、WebViewはアプリパッケージ内に含まれるJavaScriptのみをレンダリングしている。 | ✓ | ✓ |
| **6.8** | オブジェクトのデシリアライゼーションは、もしあれば、安全なシリアライゼーションAPIを使用して実装されている。 | ✓ | ✓ |

## 参考情報

OWASP モバイルセキュリティテストガイドでは、このセクションに記載されている要件を検証するための詳細な手順を提供しています。

- Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md
- iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M1 - Improper Platform Usage: https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage
- CWE: https://cwe.mitre.org/data/definitions/20.html
- CWE: https://cwe.mitre.org/data/definitions/749.html
