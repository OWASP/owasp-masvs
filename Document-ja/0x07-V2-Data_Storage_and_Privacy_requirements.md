# V2: データストレージとプライバシー要件

## 管理目標

ユーザー資格情報や個人情報などの機密データの保護はモバイルセキュリティで重要な焦点となっています。まず、IPCのようなオペレーティングシステムのメカニズムが不適切に使用されている場合、同じデバイス上で実行されている他のアプリに機密データが意図せず晒されてしまいます。また、データはクラウドストレージ、バックアップ、キーボードキャッシュから意図せず漏れることもあります。さらに、他のタイプのデバイスに比べてモバイルデバイスは簡単に紛失したり盗まれたりします。そのため、第三者が物理的にアクセスできることがより可能性の高いシナリオとなります。その場合、機密データの取得をより困難にするために追加の保護を実装することができます。

注意：MASVS はアプリ中心であるため、MDM ソリューションにより行われるようなデバイスレベルのポリシーは対象ではありません。私たちはエンタープライズのコンテキストでこのようなポリシーを使用することにより、データセキュリティをさらに強化することを推奨します。

### 機密データの定義

MASVS のコンテキストにおける機密データは、以下のように、ユーザー資格情報および特定のコンテキストにおいて機密とみなされるその他のデータの両方に関係します。

- なりすまし犯罪に悪用される可能性のある個人識別情報 (PII)：社会保障番号、クレジットカード番号、銀行口座番号、医療情報。
- 被害を受けた場合に風評被害や財務コストにつながる機密性の高いデータ：契約情報、秘密保持契約の対象となる情報、管理情報。
- 法律やコンプライアンス上の理由により保護する必要のあるすべてのデータ。

## セキュリティ検証要件

大部分のデータ開示の問題は単純なルールに従うことで防ぐことが可能です。この章に記載されているほとんどのコントロールはすべての検証レベルで必須です。

| # | MSTG-ID | 説明 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | 個人識別情報、ユーザー資格情報、暗号化鍵などの機密データを格納するために、システムの資格情報保存機能を使用している。 | x | x |
| **2.2** | MSTG-STORAGE-2 | 機密データはアプリコンテナまたはシステムの資格情報保存機能の外部に保存されていない。 | x | x |
| **2.3** | MSTG-STORAGE-3 | 機密データはアプリケーションログに書き込まれていない。 | x | x |
| **2.4** | MSTG-STORAGE-4 | 機密データはアーキテクチャに必要な部分でない限りサードパーティと共有されていない。 | x | x |
| **2.5** | MSTG-STORAGE-5 | 機密データを処理するテキスト入力では、キーボードキャッシュが無効にされている。 | x | x |
| **2.6** | MSTG-STORAGE-6 | 機密データはIPCメカニズムを介して公開されていない。 | x | x |
| **2.7** | MSTG-STORAGE-7 | パスワードやピンなどの機密データは、ユーザーインタフェースを介して公開されていない。 | x | x |
| **2.8** | MSTG-STORAGE-8 | 機密データはモバイルオペレーティングシステムにより生成されるバックアップに含まれていない。 |   | x |
| **2.9** | MSTG-STORAGE-9 | バックグラウンドへ移動した際にアプリはビューから機密データを削除している。 |  | x |
| **2.10** | MSTG-STORAGE-10 | アプリは必要以上に長くメモリ内に機密データを保持せず、使用後は明示的にメモリがクリアされている。 |  | x |
| **2.11** | MSTG-STORAGE-11 | アプリは最低限のデバイスアクセスセキュリティポリシーを適用しており、ユーザーにデバイスパスコードを設定することなどを必要としている。 |  | x |
| **2.12** | MSTG-STORAGE-12 | アプリは処理される個人識別情報の種類をユーザーに通知しており、同様にユーザーがアプリを使用する際に従うべきセキュリティのベストプラクティスについて通知している。 | x | x |
| **2.13** | MSTG-STORAGE-13 | 機密データをモバイルデバイス上のローカルに保存していない。代わりに、必要な時にリモートエンドポイントからデータを取得し、メモリ内にのみ保持している。 |  | x |
| **2.14** | MSTG-STORAGE-14 | 機密データをローカルに保存する必要がある場合には、認証が必要なハードウェア支援ストレージから取得した鍵を使用して暗号化している。 |  | x |
| **2.15** | MSTG-STORAGE-15 | 認証の試行が過度の回数にわたり失敗した後には、アプリのローカルストレージを消去している。 |  | x |

## 参考情報

OWASP モバイルセキュリティテストガイドでは、このセクションに記載されている要件を検証するための詳細な手順を提供しています。

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>
