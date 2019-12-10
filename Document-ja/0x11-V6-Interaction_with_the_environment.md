# V6: プラットフォーム連携要件

## 管理目標

アプリがセキュアな方法でプラットフォームAPIや標準コンポーネントを使用していることをこのグループのコントロールは確認します。また、コントロールはアプリ間通信(IPC)も扱います。

## セキュリティ検証要件

| # | MSTG-ID | 説明 | L1 | L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | アプリは必要となる最低限のパーミッションのみを要求している。 | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | 外部ソースおよびユーザーからの入力はすべて検証されており、必要に応じてサニタイズされている。これにはUI、インテントやカスタムURLなどのIPCメカニズム、ネットワークソースを介して受信したデータを含んでいる。 | ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | アプリはメカニズムが適切に保護されていない限り、カスタムURLスキームを介して機密な機能をエクスポートしていない。 | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | アプリはメカニズムが適切に保護されていない限り、IPC機構を通じて機密な機能をエクスポートしていない。 | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | 明示的に必要でない限りWebViewでJavaScriptが無効化されている。 | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | WebViewは最低限必要のプロトコルハンドラのセットのみを許可するよう構成されている（理想的には、httpsのみがサポートされている）。file, tel, app-id などの潜在的に危険なハンドラは無効化されている。 | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | アプリのネイティブメソッドがWebViewに公開されている場合、WebViewはアプリパッケージ内に含まれるJavaScriptのみをレンダリングしている。 | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | オブジェクトのデシリアライゼーションは、もしあれば、安全なシリアライゼーションAPIを使用して実装されている。 | ✓ | ✓ |
| **6.9** | MSTG‑PLATFORM‑9 | アプリはスクリーンオーバーレイ攻撃から自らを保護している。 (Android のみ) |  | ✓ |
| **6.10** | MSTG‑PLATFORM‑10 | WebViewを破棄する前にWebViewのキャッシュ、ストレージ、ロードされたリソース (JavaScript など) をクリアしている。 |  | ✓ |
| **6.11** | MSTG‑PLATFORM‑11 | 機密データを入力する場合は常に、アプリはカスタムサードパーティキーボードを使用できないようにしている。 |  | ✓ |
<div style="page-break-after: always;">
</div>

## 参考情報

OWASP モバイルセキュリティテストガイドでは、このセクションに記載されている要件を検証するための詳細な手順を提供しています。

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
