"""网络预测与回滚：输入、时钟与快照：待实现的核心模块。"""


def dedupe_inputs(sequences, last_sequence):
    """只接受大于已处理序号的输入。"""
    raise NotImplementedError

def reconcile(predicted, authoritative, alpha):
    """预测状态向权威状态和解。"""
    raise NotImplementedError

def tick_drift(server_tick, client_tick):
    """服务器与客户端 tick 差。"""
    raise NotImplementedError

def interp_delay(render_time, tick_time):
    """插值延迟不得为负。"""
    raise NotImplementedError

def rollback_depth(current, target, limit):
    """回滚深度限制到上限。"""
    raise NotImplementedError

def state_hash(values):
    """状态哈希只依赖状态内容。"""
    raise NotImplementedError

def resend_missing(sent, acknowledged):
    """重发未确认的输入序号。"""
    raise NotImplementedError

def is_desync(hash_a, hash_b):
    """哈希不同即 desync。"""
    raise NotImplementedError

def ring_index(tick, size):
    """快照环下标取模。"""
    raise NotImplementedError

def commit_batch(statuses):
    """批量提交全部成功才生效。"""
    raise NotImplementedError
