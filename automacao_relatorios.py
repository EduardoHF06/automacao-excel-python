import pandas as pd

# Gerando massa de dados para simular as planilhas das filiais
data_sp = pd.DataFrame({'Data': ['2026-03-01', '2026-03-02'], 'Filial': ['SP', 'SP'], 'Vendas_BRL': [1500.50, 2300.00]})
data_rj = pd.DataFrame({'Data': ['2026-03-01', '2026-03-02'], 'Filial': ['RJ', 'RJ'], 'Vendas_BRL': [1200.00, 1800.75]})
data_mg = pd.DataFrame({'Data': ['2026-03-01', '2026-03-02'], 'Filial': ['MG', 'MG'], 'Vendas_BRL': [900.20, 1100.00]})

data_sp.to_csv('vendas_sp.csv', index=False)
data_rj.to_csv('vendas_rj.csv', index=False)
data_mg.to_csv('vendas_mg.csv', index=False)

print("Iniciando consolidação dos relatórios...")

# Lendo e unindo todas as bases em uma única linha (List Comprehension)
arquivos = ['vendas_sp.csv', 'vendas_rj.csv', 'vendas_mg.csv']
df_consolidado = pd.concat([pd.read_csv(arq) for arq in arquivos], ignore_index=True)

# Calculando KPI de faturamento por filial
df_kpi = df_consolidado.groupby('Filial')['Vendas_BRL'].sum().reset_index()
df_kpi.rename(columns={'Vendas_BRL': 'Faturamento_Total'}, inplace=True)
df_kpi = df_kpi.sort_values(by='Faturamento_Total', ascending=False)

# Exportando os arquivos limpos
df_consolidado.to_csv('Base_Consolidada.csv', index=False)
df_kpi.to_csv('KPI_Faturamento.csv', index=False)

print(f"Processo finalizado. {len(df_consolidado)} linhas processadas e consolidadas.")
print("\nResumo Gerencial (Faturamento):")
print(df_kpi)
