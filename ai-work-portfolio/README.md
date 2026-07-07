# AI Work Portfolio — Agent Teams Case Study

Claude Codeの「Agent Teams」機能を初めて試した記録をまとめた、1ページのポートフォリオサイトです。
複数のAIチームメイトが役割を分担しながら並行して作業する様子を、実際のスクリーンショットとともに振り返ります。

## テーマ

- **デザイン**: `design-prompt-bold-warm-editorial.yaml` に基づく「Bold Warm Editorial」スタイル
  - 暖色ベージュ背景 × 近黒テキスト
  - 緑・コーラル・ティール・マスタードの4色をローテーションするフラットアクセント
  - 極太アッパーケースの見出し・ラベル
  - 角丸なし・ヘアラインギャップの画像グリッド
  - 画像ホバー時にキャプションがスライドインする段階的開示
  - フッターのみダーク（ink）反転のブックエンド構成

## 構成

| ファイル | 役割 |
|---|---|
| `index.html` | ページの構造（ヒーロー・イントロ・実演ギャラリー・まとめ・フッター） |
| `style.css` | 見た目のデザイン（配色・タイポグラフィ・ホバー演出） |
| `script.js` | フッターの年表示、タッチデバイス向けのキャプションタップ開閉 |
| `images/` | 実演スクリーンショット5枚 |

## 掲載内容

1. **ヒーロー**: 「AIエージェントと開発する。」の大見出しと、Agent Teams機能の紹介サブコピー
2. **イントロ（CASE STUDY）**: Agent Teams機能を試した記録であることの前置き
3. **実演ギャラリー**: 5枚のスクリーンショットとそれぞれのキャプション・学びポイント（初級→上級の順）
   - `01-agent-teams-basic.png` — BASIC / 並行タスク処理
   - `02-agent-teams-review.png` — INTERMEDIATE / マルチエージェントレビュー
   - `03-agent-teams-priority.png` — INTERMEDIATE / 優先度付け統合レポート
   - `04-agent-teams-role-plan.png` — ADVANCED / 役割分担と承認ゲート
   - `05-agent-teams-synthesis.png` — ADVANCED / 複数視点の統合判断
4. **まとめ・学び**: 4つの学びポイントをタグ風チップで表示
5. **フッター**: ダーク反転、GitHubリンク、コピーライト

## 使い方

`index.html` をブラウザで開くだけで表示されます。サーバー等のセットアップは不要です。

```
ai-work-portfolio/
├── index.html
├── style.css
├── script.js
├── README.md
└── images/
    ├── 01-agent-teams-basic.png
    ├── 02-agent-teams-review.png
    ├── 03-agent-teams-priority.png
    ├── 04-agent-teams-role-plan.png
    └── 05-agent-teams-synthesis.png
```
