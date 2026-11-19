# 网络预测与回滚：输入、时钟与快照

联机对枪时角色位置来回跳：输入没有按序号去重，预测状态没有与权威状态和解，客户端与服务器 tick 漂移，插值延迟为负，回滚深度没有上限，状态哈希不稳定，丢包后没有重发，desync 判定失效，快照环下标越界，批量提交只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
net/__init__.py
net/rollback.py
tests/test_rollback.py
```

## 当前状态

`net/rollback.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_rollback.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 输入按序号去重
2. 预测状态与权威状态和解
3. 客户端与服务器 tick 对齐
4. 插值延迟非负
5. 回滚深度限制
6. 状态哈希确定性
7. 丢包按已确认序号重发
8. desync 按哈希判定
9. 快照环下标取模
10. 批量提交统一回滚

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `net/rollback.py`
后 15 条用例应全部通过。
