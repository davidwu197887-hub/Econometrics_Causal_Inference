# Econometrics Causal Inference: A Simulation Study
> **Author:** 吴昱华 (Yuhua Wu)  
> **Contact:** [wuyh2925@mails.jlu.edu.cn](mailto:wuyh2925@mails.jlu.edu.cn)  
> **Affiliation:** 吉林大学 (Jilin University)

---

## 项目简介
本项目为一个基于 Python 开发的计量经济学实证模拟脚本。研究设计参考了**吉林大学东北亚学院周阔副教授**及其发起的**“经管学术青苗计划”**中的前沿实证范式。

通过模拟 2019–2026 年间 100 家企业的面板数据（Panel Data），本项目构建了一个虚拟政策冲击场景，并运用多种计量模型评估政策效应，旨在探索不同识别策略在处理内生性问题时的表现。

## 仓库目录
```text
Econometrics_Causal_Inference/
├── data/               存放生成的模拟数据 (sample_data.csv)
├── src/                存放源代码 (inference_demo.py)
├── output/             存放可视化图表 (parallel_trends.png)
├── .gitignore          忽略 Python 缓存及临时文件
├── requirements.txt    依赖库清单
└── README.md           说明书
