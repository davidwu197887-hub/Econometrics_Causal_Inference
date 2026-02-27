# Econometrics Causal Inference: A Simulation Study
> **Author:** 吴昱华 (Yuhua Wu)  
> **Contact:** [wuyh2925@mails.jlu.edu.cn](mailto:wuyh2925@mails.jlu.edu.cn)  
> **Affiliation:** 吉林大学 (Jilin University)

---

## 项目简介
本项目为一个基于 Python 开发的实证模拟脚本。参考**吉林大学东北亚学院周阔副教授**与其发起的团队**经管学术青苗计划**的研究成果中的计量方法与前沿实证范式。我模拟了2019–2026 年100 家企业的面板数据，用不同的模型包括Naive OLS、Panel FE、DID、IV评估一项虚拟政策冲击场景,旨在探索不同识别策略在处理内生性问题时的表现。

## 亮点展示
1. 对比Naive OLS、Panel FE和DID的特性，映射了如果不控制公司个体固定效应，政策效果会被严重误导； 
2. 生成数据阶段，为了更加仿真我引入了内生性，我设定了一个工具变量"iv_distance"（企业与当地政府的关系）作为只影响政策而不影响生产业绩的工具变量，同时我额外用IV-2SLS的方法进行稳健性检验； 
3. 绘制处理组与对照组的时间趋势图，看着更直观。

## 仓库目录
```text
Econometrics_Causal_Inference/
├── data/               存放生成的模拟数据
├── output/             存放可视化图表
├── .gitignore          忽略 Python 缓存及临时文件
├── LICENSE             开源许可
├── README.md           说明书
├── inference_demo.py   源代码脚本
└── requirements.txt     依赖库清单
