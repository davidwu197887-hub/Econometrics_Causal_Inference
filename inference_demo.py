import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS
import matplotlib.pyplot as plt

np.random.seed(2026)

# 数据生成（为了进一步仿真，引入内生性）
n_firms = 100
years = np.arange(2019, 2027) 
rows = []

for i in range(n_firms):
    # 公司固定效应
    firm_quality = np.random.normal(scale=1.0) 
    
    # 内生性：表现更好的公司更有可能被选入政策试点
    treatment_prob = 1 / (1 + np.exp(-(firm_quality + np.random.normal(0, 0.5))))
    is_treated_firm = 1 if np.random.rand() < treatment_prob else 0
    
    # 构造一个变量[比如与当地政府的关系 :) ]（只影响被政策选中概率，不直接影响业绩）
    distance_to_gov = is_treated_firm + np.random.normal(0, 0.5)

    for y in years:
        size = np.random.lognormal(mean=2.0, sigma=0.5)
        post = 1 if y >= 2023 else 0
        did = is_treated_firm * post
        
        # 模型：y = 0.5*ln(size) + 2.0*did + 公司质量 + 时间趋势 + 噪音
        noise = np.random.normal(0, 1)
        y_val = 0.5 * np.log(size) + 2.0 * did + firm_quality + 0.1 * (y - 2019) + noise
        
        rows.append({
            'firmid': i, 'year': y, 'y': y_val, 'size': size,
            'treated_group': is_treated_firm, 'post': post, 'did': did,
            'iv_distance': distance_to_gov
        })

df = pd.DataFrame(rows)

# Naive OLS (忽略内生性，通常有偏差)
X_ols = sm.add_constant(df[['did', 'post', 'treated_group', 'size']])
res_ols = sm.OLS(df['y'], X_ols).fit()
print("1.Naive OLS 结果 (可能有偏差):", res_ols.params['did'])

# Panel FE
df_panel = df.set_index(['firmid', 'year'])
mod_fe = PanelOLS.from_formula('y ~ did + size + EntityEffects', data=df_panel)
res_fe = mod_fe.fit(cov_type='clustered', cluster_entity=True)
print("2.Panel FE 结果 (更进一步):", res_fe.params['did'])

# DID 
mod_did = PanelOLS.from_formula('y ~ did + size + EntityEffects + TimeEffects', data=df_panel)
res_did = mod_did.fit(cov_type='clustered', cluster_entity=True)
print("3.DID 结果 (核心方法):", res_did.params['did'])

# IV-2SLS
mod_iv = IV2SLS.from_formula('y ~ 1 + size + [treated_group ~ iv_distance]', data=df)
res_iv = mod_iv.fit()
print("4.IV (2SLS) 结果 (检验稳健性):", res_iv.params['treated_group'])
print(res_iv.summary)

# 可视化
plt.figure(figsize=(10, 6))
df.groupby(['year', 'treated_group'])['y'].mean().unstack().plot(marker='o', ax=plt.gca())

plt.axvline(x=2022.5, color='red', linestyle='--', label='Policy Intervention (2023)')

plt.title('Parallel Trends Check (2019-2026)', fontsize=12)
plt.xlabel('Year')
plt.ylabel('Average Outcome (y)')
plt.legend(['Control Group (0)', 'Treated Group (1)', 'Policy Start (2023)'])
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
import os

if not os.path.exists('output'):
    os.makedirs('output')

plt.savefig('output/parallel_trends.png', dpi=300)
print("图表已保存至 output/parallel_trends.png")

if not os.path.exists('data'):
    os.makedirs('data')
df.to_csv('data/simulated_firm_data.csv', index=False)
plt.show()

print("\n分析完成，请看控制台及弹出图表。")
