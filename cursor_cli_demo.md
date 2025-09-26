# Cursor CLI 使用指南

Cursor CLI 是一个强大的命令行工具，可以让你在终端中直接使用 Cursor 的 AI 编码助手功能。

## 安装

```bash
curl https://cursor.com/install -fsS | bash
```

## 主要功能

### 1. 交互模式

启动交互式会话与 AI 助手对话：

```bash
# 基础启动
cursor-agent

# 带初始提示启动
cursor-agent "创建一个 Python Flask API"
```

### 2. 非交互模式（脚本模式）

适用于脚本、CI/CD 流水线或自动化任务：

```bash
# 使用 --print 参数进行非交互式执行
cursor-agent -p "分析代码中的性能问题"

# 指定输出格式
cursor-agent -p "审查安全问题" --output-format text

# 指定使用的模型
cursor-agent -p "重构这段代码" --model gpt-5
```

### 3. Shell 模式

直接在 CLI 中运行 shell 命令：

```bash
# 运行简单命令
cursor-agent "ls -la"

# 在子目录中运行命令
cursor-agent "cd src && npm test"
```

注意：Shell 模式有 30 秒超时限制，不支持长时间运行的进程。

### 4. 聊天会话管理

```bash
# 创建新的聊天会话
cursor-agent create-chat

# 列出所有聊天会话
cursor-agent ls

# 恢复最近的聊天
cursor-agent resume

# 恢复特定聊天
cursor-agent --resume <chatId>
```

### 5. MCP（模型上下文协议）支持

```bash
# 管理 MCP 服务器
cursor-agent mcp

# MCP 会自动检测 mcp.json 配置文件
```

### 6. 认证管理

```bash
# 登录
cursor-agent login

# 检查认证状态
cursor-agent status

# 登出
cursor-agent logout
```

### 7. 其他命令

```bash
# 查看版本
cursor-agent --version

# 更新到最新版本
cursor-agent update

# 安装 shell 集成（zsh）
cursor-agent install-shell-integration

# 卸载 shell 集成
cursor-agent uninstall-shell-integration
```

## 环境变量

- `CURSOR_API_KEY`: 设置 API 密钥，避免每次输入

```bash
export CURSOR_API_KEY="your-api-key"
```

## 使用示例

### 示例 1：代码审查

```bash
cursor-agent -p "审查当前目录下的 Python 代码，查找潜在的性能问题和安全漏洞"
```

### 示例 2：生成测试

```bash
cursor-agent "为 main.py 文件生成单元测试"
```

### 示例 3：重构代码

```bash
cursor-agent "将这个类重构为使用设计模式"
```

### 示例 4：在 CI/CD 中使用

```bash
#!/bin/bash
# 在 CI 流水线中自动审查代码
cursor-agent -p "检查代码质量并提供改进建议" --output-format text > code-review.txt
```

## 注意事项

1. Cursor CLI 目前处于 Beta 阶段
2. 建议仅在受信任的环境中使用
3. Shell 命令有 30 秒超时限制
4. 需要有效的 Cursor 账户和 API 密钥

## 更多信息

- 官方文档：https://docs.cursor.com/tools/cli
- Shell 模式文档：https://docs.cursor.com/cli/shell-mode
- MCP 支持文档：https://docs.cursor.com/cli/mcp