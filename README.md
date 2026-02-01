# LLM for 科研入门教程（LLM4S）

> 目标：把 **大语言模型（LLM）学习路径**、**手搓核心模块**、**多智能体框架**、**工程化微调/后训练**、与 **前沿研究（MoE-LoRA、Skills）** 放在一个集成的 GitHub 项目中，便于按阶段逐步学习上手。

---

## 你将学到什么

1. **基础知识与学习资源**：推荐阅读/课程/视频。
2. **手搓关键模块**：从 attention/transformer 到 LoRA 等参数高效微调思想。
3. **LLM 调用与（多）智能体框架**：API 调用、工具使用、LangChain 生态、agent 工作流。
4. **微调与后训练工程实践**：基于工业级开源框架完成 SFT / DPO 等。
5. **学术与应用前沿**：MoE + 参数高效微调（MoE-LoRA 等）论文/代码复现， agent skills代码级实现。

---

## 仓库结构

当前仓库主要由 5 个第三方开源项目与 1 个自行论文复现项目组成（均为学习目的收录，具体用法以各子项目 README 为准）：

```text
LLM4S/
├─ LLMs-Zero-to-Hero-master/          # 基础：手搓 Transformer / Attention 等
├─ AI-Interview-Code-master/          # 进阶：手搓 LoRA / 多头注意力等
├─ LLaMA-Factory/                     # 进阶：微调/后训练/RLHF(DPO等)
├─ Optitrust/                         # 进阶：多智能体框架搭建
├─ skills-agent-proto-main/           # 前沿：agent skill应用与定制
└─ parameter-efficient-moe-main/      # 前沿：MoE + 参数高效微调
```

---

## 参考学习路线（Roadmap）


### Stage 0：基础知识

> 这一部分主要以理论知识与基础代码操作熟悉为主，学完这一部分要求能够清晰描述大模型各相关方法的基础原理、使用方法、涉及工具等。

**LLM相关知识与面试题**

- 主要了解大语言模型相关基础理论知识
- 链接：https://wdndev.github.io/llm_interview_note/#/

**面向开发者的LLM入门教程**

- 主要了解提示词工程与langchain相关基础理论知识
- 链接：https://datawhalechina.github.io/llm-cookbook/#/


### Stage 1：手搓 Transformer
对应目录：`LLMs-Zero-to-Hero-master/`

学习目标：
- 手写 Self-Attention（含 causal mask）
- 手写 Multi-Head Attention
- 手写 Transformer Block（含 LN + residual）
- 最小可运行训练：next-token prediction

bilibili链接：https://datawhalechina.github.io/llm-cookbook/#/
github链接：https://github.com/bbruceyuan/LLMs-Zero-to-Hero


### Stage 2：参数高效微调
对应目录：`AI-Interview-Code-master/`

学习目标：
- 通过 notebook 理解并实现 LoRA：低秩分解、可训练参数量、rank/alpha 的含义
- 理解为何 LoRA 对线性层有效；如何作用在 Q/K/V/O 或 MLP 上
- 练习：给一个小型 Transformer 加上 LoRA，并验证 loss 可下降

bilibili链接：https://www.bilibili.com/video/BV1fHmkYyE2w?spm_id_from=333.788.videopod.sections&vd_source=3c467247207b06c6f382b08ef64066bf
github链接：https://github.com/bbruceyuan/AI-Interview-Code
可以直接跑的 notebook: https://openbayes.com/console/bbruceyuan/containers/RhWOr6vTLN4

### Stage 3：LLM 调用与（多）智能体框架
对应目录：`Optitrust/`

该目录为我们复现Optitrust这篇文章的多智能体框架，该文章主要搭建了一个用于OR问题自动化建模与求解的多智能体框架。由于文章没有公开代码，该代码为基于原文公开prompt另外搭建，可能实验效果与原文存在差异。文章链接如下：
https://arxiv.org/abs/2508.03117

学习目标：
- 学会通过 API 调用模型（OpenAI / 自部署 / 开源推理服务）
- 学会结构化输出（JSON schema / function calling）
- 搭建一个最小 Agent：`规划 → 执行 → 反思/修正`

另外，各大模型的API接口设置存在差异，需要阅读各大模型的开发者文档。

**官方接口平台**
- [\[ \]DeepSeek接口文档](https://api-docs.deepseek.com/zh-cn/)
- [\[ \]Qwen接口文档](https://help.aliyun.com/zh/model-studio/qwen-api-reference/)


### Stage 4：微调与后训练工程（SFT / DPO 等）
对应目录：`LLaMA-Factory/`

学习目标：
- 跑通一次 SFT（小数据、少步数，先“跑通”再追求效果）
- 理解训练配置：数据格式、tokenizer、packing、batch、lr、warmup
- 跑通一次 DPO（对比偏好数据的组织与 loss）

提示：该目录为成熟工程项目，建议把它当作“框架层或应用层”学习。在这里，你需要关注的是**如何配置环境、如何生成数据、如何设置超参、如何复现实验**，该工具提供了极其方便的UI微调与学习界面，因此你需要明确掌握应用具体方法需要实现的基本条件与数据格式。

bilibili链接：https://www.bilibili.com/video/BV1djgRzxEts/?spm_id_from=333.1387.favlist.content.click&vd_source=3c467247207b06c6f382b08ef64066bf （该课程分成了36集，详细介绍了如何使用LLaMA-Factory工具进行大模型微调）

当然，在此基础上，可以使用租借的算力平台，或者使用本地部署的大模型。因此，这里也提供了参考的大模型本地部署教程视频。

bilibili链接：https://www.bilibili.com/video/BV11ZbBeUEEo/?spm_id_from=333.1387.favlist.content.click&vd_source=3c467247207b06c6f382b08ef64066bf



### Stage 5：学术前沿（MoE + 参数高效微调）
对应目录：`parameter-efficient-moe-main/`

该部分的内容来自MoE-LoRA原文与源码，网上目前并没有该框架入门级的代码教程，因此从源码学习是最好的方法。文章链接如下:https://arxiv.org/abs/2309.05444

学习目标：
- 读懂论文设定与动机：为什么要 MoE、为什么要 PEFT、二者如何结合
- 跑通官方配置（或最小化跑通）：看懂 config、数据管线、训练/评测脚本
- 做一个小实验：对比 LoRA vs MoE-LoRA（在同一模型与数据上）

首先，需要了解MoE等方法的基础理论，bilibili教程：https://www.bilibili.com/video/BV1garHYdEoN/?spm_id_from=333.1387.favlist.content.click&vd_source=3c467247207b06c6f382b08ef64066bf

其次，b站也有对应论文的讲解视频：https://www.bilibili.com/video/BV1RHMgz4E1C/?spm_id_from=333.1387.favlist.content.click&vd_source=3c467247207b06c6f382b08ef64066bf


### Stage 6：应用前沿（agent skills）
对应目录：`skills-agent-proto-main/`

该目录提供了agent skills的详细代码集使用教程，包括定制自己的agent skill。当然，目前最火的openclaw也是领域最前沿的现象级产品，其能够基本获取计算机的权限，考虑到对于入门玩家安全防护能力不足的考虑，不建议现阶段使用该产品，因此目前不引入对应part。

bilibili链接：https://www.bilibili.com/video/BV1ZpzhBLE82
github链接：https://github.com/NanmiCoder/skills-agent-proto

---

## 环境配置

> 由于各子项目依赖不同，推荐“每个子项目单独建环境”，避免依赖冲突。

### 每个子项目独立环境
- `LLMs-Zero-to-Hero-master/`
- `AI-Interview-Code-master/`
- `LLaMA-Factory/`
- `parameter-efficient-moe-main/`
- `skills-agent-proto-main`

分别进入目录，按其 README 安装依赖与运行。


---

## 版权与致谢

本仓库包含多个第三方开源项目，仅用于学习与整理：

- `LLMs-Zero-to-Hero-master`
- `AI-Interview-Code-master`
- `LLaMA-Factory`
- `parameter-efficient-moe-main`
- `skills-agent-proto-main`


