#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def obter_resposta_sim_nao(pergunta):
    """Função auxiliar para validar entradas Sim (s) / Não (n)."""
    while True:
        resp = input(f"{pergunta} (s/n): ").strip().lower()
        if resp in ['s', 'sim', 'y', 'yes']:
            return True
        elif resp in ['n', 'nao', 'não', 'no']:
            return False
        print("Entrada inválida. Digite 's' para Sim ou 'n' para Não.")

def calculadora_ira():
    print("=" * 60)
    print("      CALCULADORA DE RISCO DE LESÃO RENAL AGUDA (IRA)")
    print("      (Uso exclusivo para pacientes internados)")
    print("=" * 60)
    
    # Informações iniciais do paciente
    nome = input("Nome ou identificador fictício do paciente: ")
    prontuario = input("Identificador fictício (não informe prontuário real): ")
    
    print(f"\nPaciente: {nome} (Prontuário: {prontuario})")
    
    # Escolha do ambiente
    print("\n--- SELEÇÃO DE LOCAL DE INTERNAÇÃO ---")
    print("1. Enfermaria")
    print("2. UTI (Unidade de Terapia Intensiva)")
    
    while True:
        local = input("O paciente está internado em qual setor? (1 para Enfermaria / 2 para UTI): ").strip()
        if local in ['1', '2']:
            break
        print("Opção inválida. Digite 1 ou 2.")
    
    score_total = 0
    detalhes_pontos = []
    
    # ----------------------------------------------------
    # ASPECTO 1: ENFERMARIA
    # ----------------------------------------------------
    if local == '1':
        print("\n" + "=" * 40)
        print(" AVALIAÇÃO: SCORE DE ENFERMARIA")
        print("=" * 40)
        
        # 1. Clinical Data
        if obter_resposta_sim_nao("1. Tem antecedentes de Diabetes Mellitus?"):
            score_total += 1
            detalhes_pontos.append("Diabetes Mellitus: +1")
            
        if obter_resposta_sim_nao("2. Tem antecedentes de Hipertensão?"):
            score_total += 1
            detalhes_pontos.append("Hipertensão: +1")
            
        if obter_resposta_sim_nao("3. Internou com Sepse?"):
            score_total += 2
            detalhes_pontos.append("Sepse na internação: +2")
            
        # 2. Admissão
        if obter_resposta_sim_nao("4. Admissão em enfermaria clínica (Responda 's' se Clínica, 'n' se Cirúrgica ou Outra)?"):
            score_total += 1
            detalhes_pontos.append("Admissão em Enfermaria Clínica: +1")
            
        # 3. Causas de Admissão
        if obter_resposta_sim_nao("5. Causa de admissão: Pneumonia?"):
            score_total += 2
            detalhes_pontos.append("Pneumonia: +2")
            
        if obter_resposta_sim_nao("6. Causa de admissão: Infecção Cutânea?"):
            score_total += 2
            detalhes_pontos.append("Infecção Cutânea: +2")
            
        if obter_resposta_sim_nao("7. Possui Desidratação?"):
            score_total += 1
            detalhes_pontos.append("Desidratação: +1")
            
        # 4. Exames laboratoriais
        if obter_resposta_sim_nao("8. Albumina sérica < 3 mg/dl?"):
            score_total += 1
            detalhes_pontos.append("Albumina sérica < 3 mg/dl: +1")
            
        if obter_resposta_sim_nao("9. Leucócitos > 15.000?"):
            score_total += 1
            detalhes_pontos.append("Leucócitos > 15.000: +1")
            
        if obter_resposta_sim_nao("10. Creatinina de base > 1.2 mg/dl?"):
            score_total += 3
            detalhes_pontos.append("Creatinina de base > 1.2 mg/dl: +3")
            
        # Resultado Enfermaria (Max: 15)
        print("\n" + "-" * 40)
        print(f"RESULTADO - SCORE DE ENFERMARIA")
        print(f"Pontuação Total: {score_total} / 15")
        print("-" * 40)
        
        if score_total >= 4:
            print("Status: [ RISCO DE IRA POSITIVO ]")
        else:
            print("Status: [ RISCO DE IRA NEGATIVO ]")

    # ----------------------------------------------------
    # ASPECTO 2: UTI
    # ----------------------------------------------------
    else:
        print("\n" + "=" * 40)
        print(" AVALIAÇÃO: UTI")
        print(" Escolha qual Score de UTI deseja rodar:")
        print(" 1. Score UTI 1 (Malhotra)")
        print(" 2. Score UTI 2 (versão simplificada inspirada no mRAI)")
        print("=" * 40)
        
        while True:
            escolha_uti = input("Digite 1 ou 2 para o score da UTI: ").strip()
            if escolha_uti in ['1', '2']:
                break
            print("Opção inválida. Digite 1 ou 2.")
        
        if escolha_uti == '1':
            print("\n--- Score UTI 1: Malhotra (Max: 21) ---")
            print("Aspectos Crônicos:")
            if obter_resposta_sim_nao("Possui doença renal crônica?"):
                score_total += 2; detalhes_pontos.append("Doença renal crônica: +2")
            if obter_resposta_sim_nao("Possui doença hepática crônica?"):
                score_total += 2; detalhes_pontos.append("Doença hepática crônica: +2")
            if obter_resposta_sim_nao("Possui Insuficiência Cardíaca Congestiva (ICC) crônica?"):
                score_total += 2; detalhes_pontos.append("ICC crônica: +2")
            if obter_resposta_sim_nao("Possui Hipertensão de base?"):
                score_total += 2; detalhes_pontos.append("Hipertensão de base: +2")
            if obter_resposta_sim_nao("Possui doença aterosclerótica coronária?"):
                score_total += 2; detalhes_pontos.append("Doença aterosclerótica coronária: +2")
                
            print("\nAspectos Agudos:")
            if obter_resposta_sim_nao("pH sérico <= 7.30?"):
                score_total += 3; detalhes_pontos.append("pH sérico <= 7.30: +3")
            if obter_resposta_sim_nao("Teve exposição à algum agente nefrotóxico?"):
                score_total += 3; detalhes_pontos.append("Exposição a agente nefrotóxico: +3")
            if obter_resposta_sim_nao("Possui infecção grave ou sepse?"):
                score_total += 2; detalhes_pontos.append("Infecção grave ou sepse: +2")
            if obter_resposta_sim_nao("Possui ventilação mecânica?"):
                score_total += 2; detalhes_pontos.append("Ventilação mecânica: +2")
            if obter_resposta_sim_nao("Possui Anemia?"):
                score_total += 1; detalhes_pontos.append("Anemia: +1")
                
            print("\n" + "-" * 40)
            print(f"RESULTADO - SCORE UTI 1 (MALHOTRA)")
            print(f"Pontuação Total: {score_total} / 21")
            print("-" * 40)
            
            if score_total >= 5:
                print("Status: [ RISCO DE IRA POSITIVO ]")
            else:
                print("Status: [ RISCO DE IRA NEGATIVO ]")
                
        elif escolha_uti == '2':
            print("\n--- Versão simplificada inspirada no mRAI (máximo codificado: 46) ---")
            print("ATENÇÃO: esta implementação não reproduz todos os componentes do estudo de Ortiz-Soriano et al. e não é validada para uso clínico.")
            
            if obter_resposta_sim_nao("Possui Diabetes de base?"):
                score_total += 1; detalhes_pontos.append("Diabetes de base: +1")
                
            if obter_resposta_sim_nao("Possui hipótese de sepse ou em uso de antibiótico?"):
                score_total += 7; detalhes_pontos.append("Sepse ou uso de antibiótico: +7")
                
            # Variação da Creatinina
            print("\nVariação da Creatinina em relação ao valor basal:")
            print("1. Subiu < 25% (0 pontos)")
            print("2. Subiu >= 25% e < 50% (11 pontos)")
            print("3. Subiu >= 50% / Subiu significativo (36 pontos)")
            
            while True:
                creat_op = input("Selecione a opção de variação da creatinina (1, 2 ou 3): ").strip()
                if creat_op == '1':
                    break
                elif creat_op == '2':
                    score_total += 11
                    detalhes_pontos.append("Aumento de creatinina 25%-50%: +11")
                    break
                elif creat_op == '3':
                    score_total += 36
                    detalhes_pontos.append("Aumento de creatinina >= 50%: +36")
                    break
                print("Opção inválida. Digite 1, 2 ou 3.")
                
            # Aumento de peso (sobrecarga hídrica)
            print("\nAumento de peso (sobrecarga hídrica) em comparação ao basal:")
            print("1. < 5% (0 pontos)")
            print("2. 5% a 9% (1 ponto)")
            print("3. >= 10% (2 pontos)")
            
            while True:
                peso_op = input("Selecione a opção de sobrecarga hídrica (1, 2 ou 3): ").strip()
                if peso_op == '1':
                    break
                elif peso_op == '2':
                    score_total += 1
                    detalhes_pontos.append("Sobrecarga hídrica 5%-9%: +1")
                    break
                elif peso_op == '3':
                    score_total += 2
                    detalhes_pontos.append("Sobrecarga hídrica >= 10%: +2")
                    break
                print("Opção inválida. Digite 1, 2 ou 3.")
                
            print("\n" + "-" * 40)
            print(f"RESULTADO - PROTÓTIPO SIMPLIFICADO INSPIRADO NO mRAI")
            print(f"Pontuação Total: {score_total} / 46 (máximo das categorias atualmente codificadas)")
            print("-" * 40)
            
            if score_total >= 10:
                print("Status: [ RISCO DE IRA POSITIVO ]")
            else:
                print("Status: [ RISCO DE IRA NEGATIVO ]")
        else:
            print("Opção de UTI inválida.")

    # Resumo detalhado dos pontos computados
    if detalhes_pontos and (local == '1' or (local == '2' and escolha_uti in ['1', '2'])):
        print("\nFatores contribuintes identificados:")
        for item in detalhes_pontos:
            print(f" - {item}")

if __name__ == "__main__":
    calculadora_ira()
