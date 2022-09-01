# V8: 耐性要件

## 管理目標

このセクションでは、機密データや機能を処理したりアクセスを与えたりするアプリに推奨される多層防御施策を取り扱います。これらのコントロールのいずれかが欠如しても脆弱性を引き起こすことはありません。代わりに、リバースエンジニアリングや特定のクライアントサイド攻撃に対する耐性を高めることを意図しています。

このセクションのコントロールは、アプリの不正改竄やコードのリバースエンジニアリングにより引き起こされるリスクのアセスメントに基づいて、必要に応じて適用する必要があります。ビジネスリスクと依存する技術的脅威にはOWASPドキュメント "Technical Risks of Reverse Engineering and Unauthorized Code Modification", "Reverse Engineering and Code Modification Prevention" （下記の参考情報を参照）を参考にすることをお勧めします。

**ソフトウェア保護はセキュリティコントロールの代わりに使用してはならないことに注意してください。MASVS-Rにリストされているコントロールは、MASVSセキュリティ要件を満たしているアプリに、脅威に特化した追加の保護コントロールを追加することを意図しています。**

以下の考慮事項が適用されます。

1. 防御されるクライアント側の脅威を明確に説明する脅威モデルを定義する必要があります。さらに、そのスキームが提供することを意図している保護グレードを明示している必要があります。例えば、明示された目標にはアプリをインストルメンテーションしようとする標的マルウェアの作者にかなりの手動リバースエンジニアリングの労力を注ぐよう強制することです。

2. 脅威モデルは合理的である必要があります。例えば、ホワイトボックス実装で暗号化鍵を隠すことは、攻撃者がホワイトボックス全体を単純にコードリフトできる場合、的外れです。

3. 保護の有効性は使用される特定のタイプの耐タンパ性および難読化のテストの経験を有する人間の専門家によって常に検証される必要があります（モバイルセキュリティテストガイドの「リバースエンジニアリング」および「ソフトウェア保護の評価」の章も参照してください）。

### 動的解析と改竄の阻止

| # | MSTG-ID | 説明 | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | アプリはユーザーに警告するかアプリを終了することでルート化デバイスや脱獄済みデバイスの存在を検知し応答している。 | x |
| **8.2** | MSTG-RESILIENCE-2 | アプリはデバッグを防止し、デバッガのアタッチを検知し応答している。利用可能なすべてのデバッグプロトコルを網羅している必要がある。 | x |
| **8.3** | MSTG-RESILIENCE-3 | アプリはそれ自身のサンドボックス内の実行ファイルや重要なデータの改竄を検知し応答している。 | x |
| **8.4** | MSTG-RESILIENCE-4 | アプリはそのデバイスで広く使用されるリバースエンジニアリングツールやフレームワークの存在を検知し応答している。 | x |
| **8.5** | MSTG-RESILIENCE-5 | アプリは任意の方法を使用してエミュレータ内で動作しているかどうかを検知し応答している。 | x |
| **8.6** | MSTG-RESILIENCE-6 | アプリはそれ自身のメモリ空間内のコードとデータの改竄を検知し応答している。 | x |
| **8.7** | MSTG-RESILIENCE-7 | アプリは各防御カテゴリ(8.1から8.6)で複数のメカニズムを実装している。耐性は使用されるメカニズムのオリジナリティの量、多様性と比例することに注意する。 | x |
| **8.8** | MSTG-RESILIENCE-8 | 検知メカニズムは遅延応答やステルス応答を含むさまざまな種類の応答をトリガーしている。 | x |
| **8.9** | MSTG-RESILIENCE-9 | 難読化はプログラムの防御に適用されており、動的解析による逆難読化を妨げている。 | x |

### デバイスバインディング

| # | MSTG-ID | 説明 | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | アプリはデバイスに固有の複数のプロパティから由来するデバイスフィンガープリントを使用して「デバイスバインディング」機能を実装している。 | x |

### 理解の阻止

| # | MSTG-ID | 説明 | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | アプリに属するすべての実行可能ファイルとライブラリはファイルレベルで暗号化されているか、実行可能ファイル内の重要なコードやデータセグメントが暗号化またはパック化されている。簡単な静的解析では重要なコードやデータは明らかにならない。 | x |
| **8.12** | MSTG-RESILIENCE-12 | 難読化の目的が機密性の高い計算を保護することである場合、現在公開されている研究を考慮して、特定のタスクに適しており手動および自動の逆難読化メソッドに対して堅牢な難読化スキームを使用している。難読化スキームの有効性は手動テストにより検証する必要がある。可能であればハードウェアベースの隔離機能が難読化より優先されることに注意する。 | x |

### 盗聴防止

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | 多層防御として、通信相手の堅牢化に加えて、アプリケーションレベルのペイロード暗号化を適用して、盗聴をより一層防止している。 | x |

## 参考情報

OWASP モバイルセキュリティテストガイドでは、このセクションに記載されている要件を検証するための詳細な手順を提供しています。

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

詳しくは以下の情報を参照してください。

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
