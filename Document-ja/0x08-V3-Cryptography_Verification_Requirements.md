# V3: 暗号化要件

## 管理目標

モバイルデバイスに保存されるデータを保護するには暗号化が重要な要素となります。特に標準的な規則に従わない場合、物事が恐ろしく誤った方向に進んでしまうカテゴリでもあります。検証されたアプリケーションが下記のような業界のベストプラクティスに従って暗号化を使用することを確認することがこの章のコントロールの目的です。

- 実績のある暗号化ライブラリの使用
- 暗号化プリミティブの適切な選択と構成
- 無作為性が必要とされる箇所での適切な乱数生成器

## セキュリティ検証要件

| # | MSTG-ID | 説明 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | アプリは暗号化の唯一の方法としてハードコードされた鍵による対称暗号化に依存していない。 | ✓ | ✓ |
| **3.2** | MSTG-CRYPTO-2 | アプリは実績のある暗号化プリミティブの実装を使用している。 | ✓ | ✓ |
| **3.3** | MSTG-CRYPTO-3 | アプリは特定のユースケースに適した暗号化プリミティブを使用している。業界のベストプラクティスに基づくパラメータで構成されている。 | ✓ | ✓ |
| **3.4** | MSTG-CRYPTO-4 | アプリはセキュリティ上の目的で広く非推奨と考えられる暗号プロトコルやアルゴリズムを使用していない。 | ✓ | ✓ |
| **3.5** | MSTG-CRYPTO-5 | アプリは複数の目的のために同じ暗号化鍵を再利用していない。 | ✓ | ✓ |
| **3.6** | MSTG-CRYPTO-6 | すべての乱数値は十分にセキュアな乱数生成器を用いて生成されている。 | ✓ | ✓ |

## 参考情報

OWASP モバイルセキュリティテストガイドでは、このセクションに記載されている要件を検証するための詳細な手順を提供しています。

- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
