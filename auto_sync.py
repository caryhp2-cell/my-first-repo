"""
auto_sync.py - 自動監控並同步到 GitHub
使用方式：python auto_sync.py
"""

import subprocess
import time
import os
from pathlib import Path

WATCH_DIR = Path(__file__).parent  # 監控目前資料夾
CHECK_INTERVAL = 60  # 每 60 秒檢查一次

def git_command(args):
    result = subprocess.run(
        ["git"] + args,
        cwd=WATCH_DIR,
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.returncode

def has_changes():
    stdout, _ = git_command(["status", "--porcelain"])
    return bool(stdout)

def auto_sync():
    print(f"🔍 開始監控資料夾：{WATCH_DIR}")
    print(f"⏱  每 1 分鐘檢查一次，有變動就自動同步\n")
    print("按 Ctrl+C 可以停止\n")

    while True:
        try:
            if has_changes():
                print("📝 偵測到變動，開始同步...")
                git_command(["add", "."])
                _, code = git_command(["commit", "-m", "auto sync"])
                if code == 0:
                    _, push_code = git_command(["push"])
                    if push_code == 0:
                        print("✅ 同步成功！\n")
                    else:
                        print("❌ Push 失敗，請檢查網路或權限\n")
                else:
                    print("⚠️  Commit 失敗\n")
            else:
                print(f"😴 無變動 ({time.strftime('%H:%M:%S')})", end="\r")

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("\n\n👋 已停止自動同步")
            break

if __name__ == "__main__":
    auto_sync()
