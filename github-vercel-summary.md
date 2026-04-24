# GitHub + Vercel 學習筆記
**日期：** 2026-04-24  
**作者：** Cary

---

## 📌 今日完成項目

1. 建立本地專案並初始化 Git
2. 推送到 GitHub Repository
3. 設定自動同步腳本
4. 部署靜態網頁到 Vercel
5. 部署靜態網頁到 GitHub Pages
6. 建立一鍵手動同步工具

---

## 🛠 使用技術

| 技術 | 用途 |
|------|------|
| Git | 版本控制，追蹤檔案變動 |
| GitHub | 雲端 Repository，存放程式碼 |
| GitHub Pages | 免費靜態網頁託管（需 Public repo） |
| Vercel | 靜態網頁 / Full-stack 應用部署 |
| Python | 撰寫自動同步腳本 |
| Windows Batch (.bat) | 一鍵手動同步 |

---

## 💻 Git 常用指令

### 初始化設定（只需做一次）
```bash
git config --global user.name "你的名字"
git config --global user.email "你的Email"
```

### 初始化 Repository
```bash
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/帳號/repo名稱.git
git branch -M main
git push -u origin main
```

### 日常使用
```bash
git add .                        # 加入所有變動
git commit -m "說明文字"          # 建立 commit
git push                         # 推送到 GitHub
git status                       # 查看目前狀態
git status --porcelain           # 簡潔查看是否有變動
```

### 常見錯誤處理
```bash
# remote origin already exists 錯誤
git remote set-url origin https://github.com/帳號/repo名稱.git
```

---

## 📄 專案檔案說明

| 檔案 | 說明 |
|------|------|
| `hello.py` | 簡單的 Python 問候程式 |
| `test.py` | 加法／減法測試程式 |
| `test2.py` | 空白測試檔（測試自動同步用） |
| `auto_sync.py` | 每 1 分鐘自動偵測變動並推送到 GitHub |
| `sync.bat` | 雙擊即可手動同步到 GitHub |
| `index.html` | 靜態網頁首頁，部署於 GitHub Pages 及 Vercel |
| `README.md` | 專案說明文件 |

---

## 🔄 自動同步腳本（auto_sync.py）

- 每 **60 秒**檢查一次資料夾是否有變動
- 有變動時自動執行 `git add . → commit → push`
- 執行方式：
```bash
python auto_sync.py
```
- 停止方式：按 `Ctrl+C`

---

## ⚡ 一鍵手動同步（sync.bat）

- 雙擊 `sync.bat` 即可立即推送所有變動到 GitHub
- 不需要開終端機，不需要輸入任何指令
- 適合不想持續監控，想到才同步的情境

---

## 🌐 部署網址

| 平台 | 網址 |
|------|------|
| GitHub Pages | https://caryhp2-cell.github.io/my-first-repo/ |
| Vercel | https://my-first-repo-nu-umber.vercel.app |

---

## 📊 GitHub Pages vs Vercel 比較

| 功能 | GitHub Pages | Vercel |
|------|:---:|:---:|
| 靜態網頁 | ✅ | ✅ |
| 免費使用 | ✅ | ✅ |
| 自動部署 | ✅ | ✅ |
| Private Repo 支援 | ❌（需付費） | ✅ |
| Full-stack / API | ❌ | ✅ |
| **適合情境** | 靜態網頁 | 靜態 + 後端 |

---

## 🔁 完整工作流程

```
修改本地檔案
     ↓
雙擊 sync.bat（或等 auto_sync.py 自動偵測）
     ↓
推送到 GitHub
     ↓
GitHub Pages & Vercel 自動偵測到新 commit
     ↓
網站自動更新完成 ✅
```

---

## 💡 重點提醒

- `git remote add origin` 只需執行一次；之後若出現 `remote origin already exists` 錯誤，改用 `git remote set-url origin <網址>`
- GitHub Pages 僅支援 **Public** repository（免費帳號）
- `auto_sync.py` 視窗必須保持開啟才能持續監控
- `sync.bat` 是按需同步，更輕量實用
- Vercel 支援 Private repo，未來開發 Full-stack 應用時使用
