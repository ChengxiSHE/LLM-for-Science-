# LLM 入门教程（LLM4S）

> 目标：把 **大语言模型（LLM）学习路径**、**手搓核心模块**、**工程化微调/后训练**、以及 **前沿研究（MoE-LoRA）** 放在一个可复用的 GitHub 项目中，便于按阶段逐步上手。

---

## 你将学到什么

本仓库按“从原理到工程，再到研究”的顺序组织内容：

1. **基础知识与学习资源**：推荐阅读/课程/视频（你可自行补充链接）。
2. **手搓关键模块**：从 attention/transformer 到 LoRA 等参数高效微调思想。
3. **LLM 调用与（多）智能体框架**：API 调用、工具使用、LangChain 生态、agent 工作流。
4. **微调与后训练工程实践**：基于工业级开源框架完成 SFT / DPO 等。
5. **学术前沿**：MoE + 参数高效微调（MoE-LoRA 等）论文/代码复现。

---

## 仓库结构

当前仓库主要由 4 个第三方开源项目组成（均为学习目的收录，具体用法以各子项目 README 为准）：

```text
LLM4S/
├─ LLMs-Zero-to-Hero-master/          # 基础：手搓 Transformer / Attention 等
├─ AI-Interview-Code-master/          # 进阶：手搓 LoRA / 多头注意力等（同一作者）
├─ LLaMA-Factory/                     # 工程：微调/后训练/RLHF(DPO等)
└─ parameter-efficient-moe-main/      # 前沿：MoE + 参数高效微调（MoE-LoRA 论文代码）
```

---

## 建议的学习路线（Roadmap）

> 你可以把它当作“课程大纲 + 实操清单”。完成每一阶段后，再进入下一阶段。

### Stage 0：基础知识（先建立地图）
- [ ] Transformer 结构：Embedding / Positional Encoding / Attention / FFN / LayerNorm / Residual
- [ ] 训练与推理：teacher forcing、mask、KV cache、采样策略
- [ ] 规模化训练常识：数据、算力、并行（DP/TP/PP）、混合精度

**可补充的学习资源（请在此处添加链接）**
- 经典文章/书：
  - [ ] 《Attention Is All You Need》
  - [ ] 《The Annotated Transformer》
- 课程/视频：
  - [ ] B 站 / YouTube / 公开课链接


### Stage 1：手搓 Transformer（从机制到代码）
对应目录：`LLMs-Zero-to-Hero-master/`

建议目标（按优先级）：
- [ ] 手写 Self-Attention（含 causal mask）
- [ ] 手写 Multi-Head Attention
- [ ] 手写 Transformer Block（含 LN + residual）
- [ ] 最小可运行训练：next-token prediction（小数据集即可）

> 备注：该子项目中包含较多环境与依赖文件（例如 `.conda/`）。建议在你自己的主仓库中**不要直接提交大型环境目录**，而是用 `requirements.txt` / `environment.yml` 管理环境（见下方“仓库瘦身建议”）。


### Stage 2：参数高效微调（LoRA 等）
对应目录：`AI-Interview-Code-master/`

建议目标：
- [ ] 通过 notebook 理解并实现 LoRA：低秩分解、可训练参数量、rank/alpha 的含义
- [ ] 理解为何 LoRA 对线性层有效；如何作用在 Q/K/V/O 或 MLP 上
- [ ] 练习：给一个小型 Transformer 加上 LoRA，并验证 loss 可下降


### Stage 3：LLM 调用与（多）智能体框架
建议在仓库中新增一个目录（你后续可创建）：

```text
agents/
├─ langchain/         # LangChain 开发文档/示例链接与最小 demo
├─ tools/             # 工具调用（检索、计算、代码执行）
└─ multi-agent/       # 多智能体协作模式（planner/executor/critic 等）
```

建议目标：
- [ ] 学会通过 API 调用模型（OpenAI / 自部署 / 开源推理服务）
- [ ] 学会结构化输出（JSON schema / function calling）
- [ ] 搭建一个最小 Agent：`规划 → 执行 → 反思/修正`

**可补充的学习资源（请在此处添加链接）**
- [ ] LangChain 文档
- [ ] OpenAI API 文档（或你使用的其他 API）
- [ ] 多智能体经典范式与项目链接


### Stage 4：微调与后训练工程（SFT / DPO 等）
对应目录：`LLaMA-Factory/`

建议目标：
- [ ] 跑通一次 SFT（小数据、少步数，先“跑通”再追求效果）
- [ ] 理解训练配置：数据格式、tokenizer、packing、batch、lr、warmup
- [ ] 跑通一次 DPO（对比偏好数据的组织与 loss）

提示：该目录为成熟工程项目，建议把它当作“框架层”学习：
- 你关注的是 **如何配置、如何组织数据、如何复现实验**，而不是每一行源码细节。


### Stage 5：学术前沿（MoE + 参数高效微调）
对应目录：`parameter-efficient-moe-main/`

建议目标：
- [ ] 读懂论文设定与动机：为什么要 MoE、为什么要 PEFT、二者如何结合
- [ ] 跑通官方配置（或最小化跑通）：看懂 config、数据管线、训练/评测脚本
- [ ] 做一个小实验：对比 LoRA vs MoE-LoRA（在同一模型与数据上）

---

## 快速开始（建议方式）

> 由于各子项目依赖不同，推荐“每个子项目单独建环境”，避免依赖冲突。

### 方式 A：每个子项目独立环境（推荐）
- `LLMs-Zero-to-Hero-master/`
- `AI-Interview-Code-master/`
- `LLaMA-Factory/`
- `parameter-efficient-moe-main/`

分别进入目录，按其 README 安装依赖与运行。

### 方式 B：统一环境（可选）
如果你希望在一个环境里跑 notebook（尤其是 Stage 1/2），可以考虑：
- Python 3.10+
- PyTorch（匹配你的 CUDA 版本）
- Jupyter / notebook

---

## 仓库瘦身建议（强烈建议在你发布到 GitHub 前处理）

当前压缩包中包含一些**不建议直接提交到主仓库**的内容：

1. `LLMs-Zero-to-Hero-master/.conda/`：体积大、可复现性差。
   - 建议：删除后用 `environment.yml` 或 `requirements.txt` 管理依赖。
2. `LLaMA-Factory/.git/`：如果你只是“收录源码”，不建议嵌套 git 仓库。
   - 建议：
     - 方式 1：删除子目录中的 `.git/`，把它当普通代码目录。
     - 方式 2：使用 `git submodule` 方式引用上游仓库。

---

## 版权与致谢（非常重要）

本仓库包含多个第三方开源项目，仅用于学习与整理：

- `LLMs-Zero-to-Hero-master`（Apache-2.0）
- `AI-Interview-Code-master`（Apache-2.0）
- `LLaMA-Factory`（以其目录内 LICENSE 为准）
- `parameter-efficient-moe-main`（以其目录内说明/许可为准）

请在使用、分发或二次开发时遵循各子项目的许可证，并在你的 README/文档中保留必要的署名与引用。

---

## 如何贡献

欢迎通过以下方式完善这个“学习型仓库”：

- 补充学习资源：论文/博客/课程/视频/实战项目链接
- 增加练习任务：每个 Stage 的“最小可运行 demo”
- 增加中文注释：对关键概念与源码模块做解释
- 提交 issue：对学习路径或代码运行问题提出反馈

---

## TODO（你可以按需调整）

- [ ] 新增 `docs/`：系统化笔记（概念图、公式、推导、FAQ）
- [ ] 新增 `agents/`：LangChain / 多智能体最小示例
- [ ] 新增 `datasets/`：练习用小数据与格式示例（避免大文件）
- [ ] 新增 `scripts/`：一键运行脚本（SFT/DPO、实验对比等）

---

## 参考链接（占位）

> 你可以把你认为最好的 GitHub/B 站链接补充到这里。

- 基础：
  - [ ] Transformer / Attention 入门
- 手搓：
  - [ ] 手写 Transformer
  - [ ] 手写 LoRA
- 工程：
  - [ ] 微调与后训练教程
- Agent：
  - [ ] LangChain / 工具调用 / 多智能体
- 前沿：
  - [ ] MoE / MoE-LoRA 论文与解读

