"""网络预测与回滚：输入、时钟与快照：核心实现。"""

import hashlib


def dedupe_inputs(sequences, last_sequence):
    """只接受大于已处理序号的输入。"""
    return [sequence for sequence in sequences if sequence > last_sequence]


def reconcile(predicted, authoritative, alpha):
    """预测状态向权威状态和解。"""
    return predicted + (authoritative - predicted) * alpha


def tick_drift(server_tick, client_tick):
    """服务器与客户端 tick 差。"""
    return server_tick - client_tick


def interp_delay(render_time, tick_time):
    """插值延迟不得为负。"""
    return max(0.0, render_time - tick_time)


def rollback_depth(current, target, limit):
    """回滚深度限制到上限。"""
    return max(0, min(limit, current - target))


def state_hash(values):
    """状态哈希只依赖状态内容。"""
    digest = hashlib.sha1(str(values).encode("utf-8")).hexdigest()
    return digest[:16]


def resend_missing(sent, acknowledged):
    """重发未确认的输入序号。"""
    return [sequence for sequence in sent if sequence not in acknowledged]


def is_desync(hash_a, hash_b):
    """哈希不同即 desync。"""
    return hash_a != hash_b


def ring_index(tick, size):
    """快照环下标取模。"""
    return tick % size


def commit_batch(statuses):
    """批量提交全部成功才生效。"""
    return all(statuses)
