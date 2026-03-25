"""
Agente de Conformidade (Compliance)
==================================

Arquitetura de agente CrewAI para garantir conformidade regulatória
em marketing e uso de dados em múltiplas jurisdições.

Autor: AI Marketing Team
Versão: 1.0.0
"""

from crewai import Agent
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class ComplianceAgent:
    """
    Agente especializado em garantir que todas as peças de marketing
    e uso de dados estejam em conformidade com:
    - GDPR (União Europeia)
    - LGPD (Brasil)
    - CCPA (Califórnia, EUA)
    - Regulamentações locais de cada mercado
    """

    def __init__(self):
        self.role = "Especialista em Conformidade e Regulamentação"
        self.goal = "Garantir que todas as comunicações de marketing e práticas de uso de dados estejam 100% em conformidade com as regulamentações aplicáveis em cada mercado"
        self.backstory = """
        Você é um especialista jurídico em proteção de dados e conformidade regulatória 
        com mais de 15 anos de experiência em ajuda empresas de tecnologia a navegar 
        pelo complexo cenário regulatório global.
        
        Formado em Direito pela USP com MBA em Direito Digital pela London School of 
        Economics, você já ajudou dezenas de startups de SaaS a expandir globalmente 
        enquanto mantinham plena conformidade legal.
        
        Você conhece cada vírgula do GDPR, LGPD e CCPA, e sabe como adaptar 
        práticas de marketing para diferentes jurisdições sem comprometer 
        a eficácia das campanhas.
        
        Sua missão é proteger a empresa de riscos regulatórios enquanto 
        permite que o marketing opere de forma ágil e eficiente.
        """

    def criar_agente(self) -> Agent:
        """Cria e retorna o agente de Compliance."""
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True,
            max_iterations=5
        )

    def validar_conteudo_marketing(
        self,
        conteudo: str,
        regiao: str,
        tipo_midia: str
    ) -> Dict[str, Any]:
        """
        Valida se o conteúdo de marketing está em conformidade.

        Args:
            conteudo: Conteúdo a ser validado
            regiao: Região/jurisdição
            tipo_midia: Tipo de mídia (ads, email, blog, etc)

        Returns:
            Dict: Resultado da validação de compliance
        """
        requisitos_por_regiao = {
            "BR": {
                "lei": "LGPD (Lei 13.709/2018)",
                "requisitos": [
                    "Consentimento explícito para coleta de dados",
                    "Política de privacidade acessível",
                    "Direito de exclusão de dados",
                    "Finalidade clara do tratamento"
                ],
                "multas": "Até 2% do faturamento (max R$ 50M)"
            },
            "US": {
                "lei": "CCPA/CPRA (Califórnia)",
                "requisitos": [
                    "Direito de recusa (opt-out)",
                    "Divulgação de coleta de dados",
                    "Não discriminação por exercício de direitos",
                    "Acordo de não venda (se aplicável)"
                ],
                "multas": "Até US$ 7.500 por violação intencional"
            },
            "EU": {
                "lei": "GDPR (Regulamento 2016/679)",
                "requisitos": [
                    "Base legal para processamento",
                    "Consentimento granular",
                    "Data Protection Impact Assessment",
                    "Designação de DPO (se aplicável)",
                    "Registro de atividades de tratamento"
                ],
                "multas": "Até 4% do faturamento global ou EUR 20M"
            }
        }

        requisitos = requisitos_por_regiao.get(
            regiao,
            requisitos_por_regiao["BR"]
        )

        # Análise simulada - em produção usaria LLM
        alertas = self._identificar_alertas(conteudo, requisitos)

        return {
            "conteudo": conteudo,
            "regiao": regiao,
            "lei_aplicavel": requisitos["lei"],
            "conforme": len(alertas) == 0,
            "alertas_encontrados": alertas,
            "recomendacoes": self._gerar_recomendacoes(alertas),
            "riscos_identificados": self._avaliar_riscos(alertas, requisitos),
            "aprovado": len(alertas) == 0,
            "versao_corrigida": self._gerar_correcao(conteudo, alertas) if alertas else conteudo
        }

    def _identificar_alertas(self, conteudo: str, requisitos: Dict) -> List[str]:
        """Identifica alertas de compliance no conteúdo."""
        alertas = []

        # Verificações simuladas
        palavras_problematicas = [
            "garantia", "certamente", "sempre", "nunca falha",
            "100%", "garantido", "sem risco"
        ]

        for palavra in palavras_problematicas:
            if palavra.lower() in conteudo.lower():
                alertas.append(
                    f"Palavra potencialmente problemática: '{palavra}' - "
                    "pode configurar promessa de rendimento proibida"
                )

        return alertas

    def _gerar_recomendacoes(self, alertas: List[str]) -> List[str]:
        """Gera recomendações de correção."""
        return [
            "Usar linguagem prospectiva em vez de garantias",
            "Incluir disclaimers apropriados",
            "Revisar com time jurídico local"
        ] if alertas else []

    def _avaliar_riscos(self, alertas: List[str], requisitos: Dict) -> List[Dict]:
        """Avalia o nível de risco dos alertas."""
        return [{
            "alerta": a,
            "nivel_risco": "Médio" if alertas else "Nenhum",
            "acao_requerida": "Revisão jurídica" if alertas else "Aprovado"
        } for a in alertas]

    def _gerar_correcao(self, conteudo: str, alertas: List[str]) -> str:
        """Gera versão corrigida do conteúdo."""
        # Simulação de correção
        return f"{conteudo} [VERSÃO REVISADA - Adicionar disclaimer]"

    def validar_uso_dados_pessoais(
        self,
        fonte_dados: str,
        finalidade: str,
        regiao: str
    ) -> Dict[str, Any]:
        """
        Valida o uso de dados pessoais conforme regulamentação.

        Args:
            fonte_dados: Origem dos dados (formulário, cookie, etc)
            finalidade: Finalidade do uso dos dados
            regiao: Região/jurisdição

        Returns:
            Dict: Resultado da validação
        """
        bases_legais = {
            "BR": ["Consentimento", "Legítimo interesse", "Execução de contrato"],
            "US": ["Consentimento", "Opt-out notice", "Serviço prestado"],
            "EU": [
                "Consentimento (Art. 6(1)(a))",
                "Execução de contrato (Art. 6(1)(b))",
                "Obrigação legal (Art. 6(1)(c))",
                "Interesse legítimo (Art. 6(1)(f))"
            ]
        }

        return {
            "fonte_dados": fonte_dados,
            "finalidade": finalidade,
            "regiao": regiao,
            "bases_legais_permitidas": bases_legais.get(regiao, []),
            "conformidade": "Verde",
            "documentacao_requerida": [
                "Registro de consentimento",
                "Política de privacidade atualizada",
                "Procedimento de exercício de direitos"
            ]
        }

    def gerar_clausulas_legais(
        self,
        tipo_documento: str,
        regiao: str
    ) -> str:
        """
        Gera cláusulas legais padrão para documentos de marketing.

        Args:
            tipo_documento: Tipo (termos, privacidade, cookies)
            regiao: Região alvo

        Returns:
            str: Texto da cláusula gerada
        """
        templates = {
            "BR": {
                "privacidade": """
                Política de Privacidade
                =======================
                Seus dados são tratados conforme a Lei Geral de Proteção de 
                Dados Pessoais (LGPD - Lei 13.709/2018).
                
                Finalidade: [descrever finalidade]
                Tempo de retenção: [definir período]
                Seus direitos: acesso, correção, exclusão, portabilidade
                
                Contato: privacidade@seudominio.com.br
                """,
                "cookies": "Utilizamos cookies para melhorar sua experiência..."
            },
            "EU": {
                "privacidade": """
                Privacy Policy
                ==============
                Your data is processed in accordance with the General Data 
                Protection Regulation (GDPR - EU 2016/679).
                
                Legal basis: [describebasis]
                Retention period: [definir período]
                Your rights: access, rectification, erasure, portability, 
                           restriction, objection, data portability
                
                Contact: privacy@yourdomain.com
                Data Protection Officer: dpo@yourdomain.com
                """,
                "cookies": "We use cookies to enhance your browsing experience..."
            }
        }

        return templates.get(regiao, templates["BR"]).get(
            tipo_documento,
            "Template não disponível"
        )


def main():
    """Função de teste do agente."""
    agente = ComplianceAgent()
    agente_criado = agente.criar_agente()

    print(f"Agente: {agente_criado.role}")

    # Teste de validação
    resultado = agente.validar_conteudo_marketing(
        "Garanta 100% de sucesso em seu fluxo de caixa!",
        "BR",
        "ads"
    )
    print(f"Conformidade: {resultado['lei_aplicavel']}")
    print(f"Aprovado: {resultado['aprovado']}")


if __name__ == "__main__":
    main()
