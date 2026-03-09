Automação de Relatórios Consolidados com Python

## O Problema de Negócio
Rotinas operacionais e de suporte frequentemente exigem que analistas gastem horas copiando e colando informações de dezenas de planilhas diferentes (Excel/CSV) para montar uma única base de dados. Isso gera perda de produtividade e margem para erro humano.

Este projeto resolve essa dor através de um script de automação focado em **ganho de tempo e precisão na geração de KPIs**.

## Tecnologias Utilizadas
* **Python 3** (Lógica de automação e varredura de arquivos)
* **Pandas** (Leitura, consolidação e cálculo de métricas)
* **OS / Sistema de Arquivos** (Manipulação de múltiplos relatórios)

## Como a automação funciona na prática
Em vez de realizar o trabalho manualmente, o script executa o seguinte pipeline:
1. **Varredura:** Lê múltiplos arquivos `.csv` simulando relatórios diários de diferentes filiais.
2. **Consolidação:** Une todas as planilhas fragmentadas em um único *DataFrame* robusto e estruturado.
3. **Cálculo de KPI:** Aplica funções de agrupamento (`groupby`) para calcular automaticamente o faturamento total gerado por filial.
4. **Exportação:** Gera automaticamente os arquivos finais limpos (`Base_Consolidada_Final.csv` e `KPI_Resumo_Gerencial.csv`), prontos para serem apresentados à diretoria ou importados no Power BI/Excel.

## mpacto do Projeto
O que antes levaria horas de trabalho braçal ao longo de um mês, agora é executado em menos de **1 segundo**. Este case demonstra a aplicação direta da programação para otimizar fluxos de trabalho do dia a dia corporativo, liberando a equipe de suporte e análise para focar em tarefas mais estratégicas.

## Como testar o script
1. Clone este repositório: `git clone https://github.com/EduardoHF06/automacao-excel-python.git`
2. Instale o Pandas: `pip install pandas`
3. Execute o código: `python automacao_relatorios.py`
