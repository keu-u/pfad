import pandas as pd
import plotly.express as px
import os

# 读取每个 CSV 文件
df1 = pd.read_csv('/Users/trxye./Desktop/nature data/data1.csv')
df2 = pd.read_csv('/Users/trxye./Desktop/nature data/data2.csv')
df3 = pd.read_csv('/Users/trxye./Desktop/nature data/data3.csv')
df4 = pd.read_csv('/Users/trxye./Desktop/nature data/data4.csv')

# 合并数据
df_combined = pd.concat([df1, df2, df3, df4], ignore_index=True)

# 确认年份列是 'umd_tree_cover_loss__year'，数据列为 'umd_tree_cover_loss__ha'
print("DataFrame Columns:", df_combined.columns)

# 假设年份列为 'umd_tree_cover_loss__year'，将其转换为 datetime
df_combined['umd_tree_cover_loss__year'] = pd.to_datetime(df_combined['umd_tree_cover_loss__year'], format='%Y')

# 创建 Plotly 动态图表
fig = px.line(df_combined, x='umd_tree_cover_loss__year', y='umd_tree_cover_loss__ha', 
              title='Global Annual Tree Cover Loss',
              labels={'umd_tree_cover_loss__year': 'Year', 'umd_tree_cover_loss__ha': 'Tree Cover Loss (ha)'})

# 添加艺术效果
fig.update_traces(line=dict(width=2, color='green'), mode='lines+markers')
fig.update_layout(title='Dynamic Visualization of Global Tree Cover Loss',
                  xaxis_title='Year',
                  yaxis_title='Tree Cover Loss (ha)',
                  plot_bgcolor='rgba(240,240,240,0.8)',
                  paper_bgcolor='white',
                  font=dict(size=12))

# 显示图表
fig.show()
