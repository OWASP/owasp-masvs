# V4: 認証とセッション管理要件

## 管理目標

多くの場合、リモートサービスへのユーザーログインはモバイルアプリアーキテクチャ全体の不可欠な要素です。ロジックの大半はエンドポイントで発生しますが、MASVSではユーザーアカウントとセッションの管理方法に関するいくつかの基本的な要件を定義します。

## セキュリティ検証要件

| # | MSTG-ID | 説明 | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | アプリがユーザーにリモートサービスへのアクセスを提供する場合、ユーザー名/パスワード認証など何らかの形態の認証がリモートエンドポイントで実行されている。 | x | x |
| **4.2** | MSTG-AUTH-2 | ステートフルなセッション管理を使用する場合、リモートエンドポイントはランダムに生成されたセッション識別子を使用し、ユーザーの資格情報を送信せずにクライアントリクエストを認証している。 | x | x |
| **4.3** | MSTG-AUTH-3 | ステートレスなトークンベースの認証を使用する場合、サーバーはセキュアなアルゴリズムを使用して署名されたトークンを提供している。 | x | x |
| **4.4** | MSTG-AUTH-4 | ユーザーがログアウトする際に、リモートエンドポイントは既存のセッションを終了している。 | x | x |
| **4.5** | MSTG-AUTH-5 | パスワードポリシーが存在し、リモートエンドポイントで実施されている。 | x | x |
| **4.6** | MSTG-AUTH-6 | リモートエンドポイントは過度な資格情報の送信に対する保護を実装している。 | x | x |
| **4.7** | MSTG-AUTH-7 | 事前に定義された非アクティブ期間およびアクセストークンの有効期限が切れた後に、セッションはリモートエンドポイントで無効にしている。 | x | x |
| **4.8** | MSTG-AUTH-8 | 生体認証が使用される場合は（単に「true」や「false」を返すAPIを使うなどの）イベントバインディングは使用しない。代わりに、キーチェーンやキーストアのアンロックに基づいている。 |  | x |
| **4.9** | MSTG-AUTH-9 | リモートエンドポイントに二要素認証が存在し、リモートエンドポイントで二要素認証要件が一貫して適用されている。 |  | x |
| **4.10** | MSTG-AUTH-10 | 機密トランザクションはステップアップ認証を必要としている。 |  | x |
| **4.11** | MSTG-AUTH-11 | アプリはユーザーのアカウントでのすべての機密アクティビティをユーザーに通知している。ユーザーはデバイスの一覧を表示したり、コンテキスト情報 (IP アドレス、位置情報など) を表示したり、特定のデバイスをブロックすることができる。 |  | x |
| **4.12** | MSTG-AUTH-12 | 認可モデルはリモートエンドポイントで定義および実施されている。 | x | x |

## 参考情報

OWASP モバイルセキュリティテストガイドでは、このセクションに記載されている要件を検証するための詳細な手順を提供しています。

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
