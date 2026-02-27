作者：吴昱华 wuyh2925@mails.jlu.edu.cn

仓库目录：
Econometrics_Causal_Inference/
├── data/               存放生成的模拟数据
│   └── sample_data.csv
├── src/                存放源代码
│   └── inference_demo.py
├── output/             存放生成的图表
│   └── parallel_trends.png
├── .gitignore          忽略不需要的文件
├── requirements.txt    依赖库清单
└── README.md           说明书

项目简介
这是我这段时间参照吉林大学周阔副教授与其发起的团队“经管学术青苗计划” 的研究成果中用到的实证方法并自学Python编程写的一个模拟脚本。我模拟了2019–2026 年100 家企业的面板，用不同的模型包括Naive OLS、Panel FE、DID、IV评估一项虚拟政策

亮点
1. 对比Naive OLS、Panel FE和DID的特性，映射了如果不控制公司个体固定效应，政策效果会被严重误导；
2. 生成数据阶段，为了更加仿真我引入了内生性，我设定了一个工具变量"iv_distance"（企业与当地政府的关系）作为只影响政策而不影响生产业绩的工具变量，同时我额外用IV-2SLS的方法进行稳健性检验；
3. 绘制处理组与对照组的时间趋势图，看着更直观。

运行方法
1. 安装依赖库：`pip install pandas linearmodels statsmodels matplotlib`
2. 运行：`inference_demo.py