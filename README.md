# Calculadora de Risco de Injúria Renal Aguda (IRA / AKI)

Calculadora clínica interativa em Python desenvolvida para triagem de pacientes internados, auxiliando na predição de risco de Lesão Renal Aguda tanto em ambiente de **Enfermaria** quanto em **UTI**.

---

## Escalas e Modelos Clínicos Utilizados

O sistema implementa três escores validados pela literatura nefrológica:

1. **Enfermaria** (*Acute Kidney Injury Prediction Score Model*)
   * **Referência:** *Clin Nephrol. 2021 Apr;95(4):182-188*.
   * **Critério de Corte:** $\ge 4$ pontos (Risco Positivo) / Máximo de 15 pontos.
2. **UTI - Score 1 (Malhotra)**
   * **Referência:** *Nephrol Dial Transplant. 2017 May 1;32(5):814-822*.
   * **Critério de Corte:** $\ge 5$ pontos (Risco Positivo) / Máximo de 21 pontos.
3. **UTI - Score 2 (MRAI Modificado por Ortiz-Soriano)**
   * **Referência:** *Nephrol Dial Transplant. 2022 Apr 25;37(5):895-903*.
   * **Critério de Corte:** $\ge 10$ pontos (Risco Positivo) / Máximo de 50 pontos (inclui graduação de variação de creatinina e sobrecarga hídrica ponderal).

---

## Funcionalidades do Script

* **Validação de Entrada:** Tratamento rigoroso de inputs para evitar falhas de digitação no terminal.
* **Fluxo Condicional Dinâmico:** Direciona o fluxo automaticamente com base no setor de internação do paciente.
* **Auditoria de Resposta:** Gera um resumo detalhado ao final da execução listando exatamente quais critérios somaram pontos para o escore do paciente.

---

## Como Executar

Certifique-se de ter o Python 3 instalado em seu sistema. 

1. Clone o repositório ou baixe o arquivo do script (`calculadora_ira.py`):
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio
