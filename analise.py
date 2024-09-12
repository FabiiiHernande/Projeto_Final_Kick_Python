from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=19)
        self.cell(0, 60, label.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text.encode('latin-1', 'replace').decode('latin-1'))
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()


pdf.add_page()

pdf.titulo("Análise dos Dados da Desigualdade Educacional no Brasil.")
pdf.sub_titulo("Foco da análise na regiões sudeste e nordeste do Brasil")
pdf.imagem("capa.jpeg", 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada("Autora: Fabiana Hernande")
pdf.linha_centralizada("Data: 10 de Setembro de 2024")
pdf.linha_centralizada("Fonte: mec.gov") 


# ------------- 1 pagina -------------
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("A desigualdade na educação universitária brasileira é um reflexo das complexas questões sociais e econômicas que o país enfrenta. Apesar dos avanços significativos nas últimas décadas, a disparidade persiste em várias dimensões do sistema educacional, afetando o acesso, a qualidade e os resultados da educação para diferentes grupos de pessoas. Este relatório visa analisar dados recentes para entender melhor essas desigualdades e propor soluções que possam contribuir para um sistema educacional mais equitativo.")

pdf.paragrafo("A análise de dados sobre a educação universitária no Brasil revela que, embora mais da metade da população brasileira acima de 25 anos tenha concluído o ensino médio, ainda existem barreiras significativas para o acesso ao ensino superior. Fatores como a necessidade de trabalhar, a falta de recursos financeiros e as desigualdades raciais e regionais continuam a limitar as oportunidades educacionais para muitos brasileiros. Este relatório examina essas barreiras e como elas impactam a trajetória educacional dos estudantes.")

pdf.paragrafo("O compromisso com a igualdade educacional é fundamental para criar um país mais justo, produtivo e próspero. Ao analisar os dados sobre a educação universitária, este relatório busca identificar as áreas que necessitam de intervenção e propor políticas públicas que possam reduzir as desigualdades. Acreditamos que, ao enfrentar esses desafios de forma direta e informada, podemos construir um sistema educacional que ofereça oportunidades iguais para todos os brasileiros, independentemente de sua origem social, econômica ou racial.")

pdf.imagem("grafico_01.png", 30, 175, 150)
pdf.ln(120)

pdf.paragrafo("Com base na análise inicial do gráfico acima é revelada uma distribuição desigual das vagas universitárias entre as regiões brasileiras. A região Sudeste concentra a maior parte das vagas, com 40,5%, destacando-se como o principal polo educacional do país. Em contraste, a região Nordeste possui 21,2% das vagas, seguida pelo Sul com 16,4%, Norte com 11,1% e Centro-Oeste com 10,8%. A categoria Ignorado/Exterior representa apenas 0,1% das vagas. Esses dados evidenciam a necessidade de políticas públicas que promovam uma distribuição mais equitativa das oportunidades educacionais em todo o Brasil, visando reduzir as disparidades regionais e garantir um acesso mais igualitário ao ensino superior.")

# ------------- 2 pagina -------------

pdf.titulo_base("Número de vagas na região Sudeste do Brasil")

pdf.paragrafo("O próximo gráfico destaca a distribuição das vagas universitárias entre os estados de Espírito Santo (ES), Minas Gerais (MG), Rio de Janeiro (RJ) e São Paulo (SP). A visualização revela que São Paulo lidera com uma quantidade significativa de vagas, refletindo sua posição como o estado mais populoso e economicamente desenvolvido da região. Este dado é crucial para entender a concentração de oportunidades educacionais e a necessidade de políticas que possam equilibrar essa distribuição.")

pdf.ln(93)
pdf.imagem("grafico_02.png", 30, 150, 130)

pdf.paragrafo("Minas Gerais aparece como o segundo estado com o maior número de vagas universitárias na região Sudeste. Este estado, conhecido por suas diversas instituições de ensino superior, desempenha um papel importante na formação acadêmica e profissional de muitos brasileiros. A análise dos dados de Minas Gerais pode fornecer insights valiosos sobre como melhorar ainda mais o acesso e a qualidade da educação superior no estado.")

pdf.paragrafo("Os estados do Rio de Janeiro e Espírito Santo, embora com um número menor de vagas em comparação a São Paulo e Minas Gerais, também são fundamentais para a oferta educacional na região Sudeste. O Rio de Janeiro, com suas renomadas universidades, e o Espírito Santo, com seu crescimento constante no setor educacional, contribuem significativamente para a diversidade e a qualidade do ensino superior na região. Este gráfico evidencia a importância de uma análise detalhada para identificar áreas de melhoria e promover uma distribuição mais equitativa das vagas universitárias em toda a região Sudeste.")



#--------3 página ------

pdf.titulo_base("Número de vagas na região Nordeste do Brasil")

pdf.paragrafo("O gráfico baixo ilustra a distribuição das vagas universitárias entre os estados dessa região. A Bahia se destaca como o estado com a maior porcentagem de vagas, representando 30,8% do total. Esse dado reflete a importância da Bahia como um centro educacional significativo no Nordeste, abrigando diversas instituições de ensino superior que atraem estudantes de várias partes do país.")
pdf.ln(93)
pdf.imagem("grafico_03.png", 40, 130, 130)

pdf.paragrafo("Outros estados como Pernambuco e Ceará também possuem uma quantidade considerável de vagas universitárias, com 16,5% e 14,8%, respectivamente. Esses estados são conhecidos por suas universidades renomadas e programas de pesquisa, contribuindo significativamente para a formação acadêmica e profissional na região. A presença de um número expressivo de vagas nesses estados indica um esforço contínuo para expandir o acesso ao ensino superior e melhorar a qualidade da educação.")

pdf.paragrafo("Por outro lado, estados como Alagoas, Piauí e Sergipe apresentam porcentagens menores de vagas universitárias, com 4,8%, 4,7% e 3,5%, respectivamente. Essa disparidade evidencia a necessidade de políticas públicas que promovam uma distribuição mais equitativa das oportunidades educacionais. Investir na expansão das vagas universitárias nesses estados pode contribuir para reduzir as desigualdades regionais e garantir que mais estudantes tenham acesso a uma educação superior de qualidade, independentemente de sua localização geográfica.")


# ------------- 4 pagina -------------
pdf.titulo_base("Vagas por Modalidade de Ensino")
pdf.imagem("grafico_04.png", 40, 75, 110)
pdf.ln(70)
pdf.paragrafo("Os gráficos revelam uma predominância esmagadora da Educação a Distância nas duas regiões analisadas, que representa 99,8% das vagas disponíveis. Em contraste, a Educação Presencial ocupa apenas 0,2% das vagas. Esses dados indicam que a oferta educacional na regiões é majoritariamente voltada para o ensino a distância, refletindo possivelmente uma preferência às vantagens de flexibilidade e acessibilidade que essa modalidade pode oferecere e seu custo mais baixo.")
pdf.ln(93)
pdf.imagem("grafico_05.png", 40, 205, 110)


# ------------- 5 pagina -------------

pdf.titulo_base("Conclusão")

pdf.paragrafo("A análise dos dados sobre a distribuição de vagas universitárias nas regiões Sudeste e Nordeste do Brasil revela importantes insights sobre as disparidades e desafios enfrentados pelo sistema educacional brasileiro. No Sudeste, a predominância de vagas está concentrada em São Paulo, que lidera com uma quantidade significativa de oportunidades educacionais. Minas Gerais e Rio de Janeiro também se destacam, contribuindo para a alta concentração de vagas na região. Em contraste, o Espírito Santo apresenta um número menor de vagas, evidenciando uma distribuição desigual mesmo dentro da região.")

pdf.paragrafo("No Nordeste, a Bahia se sobressai como o estado com a maior porcentagem de vagas universitárias, seguido por Pernambuco e Ceará. Esses estados são fundamentais para a oferta educacional na região, mas ainda há uma disparidade significativa quando comparados ao Sudeste. Estados como Alagoas, Piauí e Sergipe possuem uma quantidade menor de vagas, o que indica a necessidade de políticas públicas que promovam uma distribuição mais equitativa das oportunidades educacionais.")

pdf.paragrafo("A comparação entre as duas regiões destaca a concentração de vagas no Sudeste, especialmente em São Paulo, que sozinho representa uma parcela considerável das vagas disponíveis. Essa concentração pode ser atribuída ao desenvolvimento econômico e à infraestrutura educacional mais robusta da região. No entanto, essa disparidade também aponta para a necessidade de investimentos em outras regiões para equilibrar a oferta educacional e garantir que mais estudantes tenham acesso a uma educação superior de qualidade.")

pdf.paragrafo("No Nordeste, a distribuição das vagas é mais fragmentada, com alguns estados concentrando a maioria das oportunidades. A Bahia, por exemplo, lidera com 30,8% das vagas, enquanto outros estados possuem porcentagens significativamente menores. Essa fragmentação pode ser um reflexo das desigualdades socioeconômicas e da infraestrutura educacional menos desenvolvida em algumas áreas. Investir na expansão das vagas universitárias em estados com menor oferta pode contribuir para reduzir essas desigualdades e promover um desenvolvimento mais equilibrado na região.")

pdf.paragrafo("Em conclusão, a análise dos dados das regiões Sudeste e Nordeste evidencia a necessidade de políticas públicas que promovam uma distribuição mais equitativa das vagas universitárias em todo o Brasil. Enquanto o Sudeste se destaca pela concentração de vagas em estados como São Paulo, o Nordeste apresenta uma distribuição mais fragmentada, com estados como a Bahia liderando a oferta educacional. Para garantir um acesso mais igualitário ao ensino superior, é fundamental investir em infraestrutura educacional e políticas de inclusão que beneficiem todas as regiões do país, promovendo um desenvolvimento mais justo e equilibrado.")

pdf.output("relatório.pdf")