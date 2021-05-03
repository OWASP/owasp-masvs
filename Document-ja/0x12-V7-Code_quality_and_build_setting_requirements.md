# V7: コード品質とビルド設定要件

## 管理目標

アプリの開発で基本的なセキュリティコーディングプラクティスに従っており、コンパイラが提供する「フリー」のセキュリティ機能が有効になっていることを確認することがこのコントロールの目標です。

## セキュリティ検証要件

| # | MSTG-ID | 説明 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | アプリは有効な証明書で署名およびプロビジョニングされている。その秘密鍵は適切に保護されている。 | x | x |
| **7.2** | MSTG-CODE-2 | アプリはリリースモードでビルドされている。リリースビルドに適した設定である（デバッグ不可など）。 | x | x |
| **7.3** | MSTG-CODE-3 | デバッグシンボルはネイティブバイナリから削除されている。 | x | x |
| **7.4** | MSTG-CODE-4 | デバッグコードおよび開発者支援コード (テストコード、バックドア、隠し設定など) は削除されている。アプリは詳細なエラーやデバッグメッセージをログ出力していない。 | x | x |
| **7.5** | MSTG-CODE-5 | モバイルアプリで使用されるライブラリ、フレームワークなどのすべてのサードパーティコンポーネントを把握し、既知の脆弱性を確認している。 | x | x |
| **7.6** | MSTG-CODE-6 | アプリは可能性のある例外をキャッチし処理している。 | x | x |
| **7.7** | MSTG-CODE-7 | セキュリティコントロールのエラー処理ロジックはデフォルトでアクセスを拒否している。 | x | x |
| **7.8** | MSTG-CODE-8 | アンマネージドコードでは、メモリはセキュアに割り当て、解放、使用されている。 | x | x |
| **7.9** | MSTG-CODE-9 | バイトコードの軽量化、スタック保護、PIEサポート、自動参照カウントなどツールチェーンにより提供されるフリーのセキュリティ機能が有効化されている。 | x | x |

## 参考情報

OWASP モバイルセキュリティテストガイドでは、上記の要件を検証するための詳細な手順を提供しています。

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
