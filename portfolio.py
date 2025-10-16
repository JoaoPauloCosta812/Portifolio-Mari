import streamlit as st
from PIL import Image
import os

# ---------------- CONFIGURAÇÃO ----------------
st.set_page_config(
    page_title="Portfólio | Mariele Coelho",
    page_icon="💼",
    layout="wide"
)

# ---------------- CARREGAR IMAGEM (com fallback) ----------------
img_path = r"C:\Users\paulo\OneDrive\Área de Trabalho\Portifolio M\foto_perfil.png"
imagem = None
if os.path.exists(img_path):
    try:
        imagem = Image.open(img_path)
    except Exception as e:
        imagem = None
        # opcional: você pode logar o erro se quiser
else:
    imagem = None

# Se a imagem não foi encontrada, cria um placeholder simples (opcional)
if imagem is None:
    # cria uma imagem em branco 260x260 (pode ajustar)
    imagem = Image.new("RGB", (260, 260), color=(240, 240, 240))

# ---------------- CSS PERSONALIZADO ----------------
st.markdown("""
    <style>
        html, body, [class*="stApp"] {
            background-color: #f8f9fa;
            color: #333;
            font-family: 'Lato', sans-serif;
        }

        h1, h2, h3 {
            color: #1a2a44;
        }

        /* Cabeçalho em duas colunas */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1100px;
            margin: 3rem auto 3rem auto;
            background: white;
            padding: 2.5rem 3rem;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        .header-text {
            flex: 1;
            padding-right: 2rem;
        }

        .name {
            font-size: 52px;
            font-weight: 800;
            color: #1a2a44;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            font-size: 22px;
            color: #5f5f5f;
            margin-bottom: 1.5rem;
        }

        .intro {
            font-size: 17px;
            line-height: 1.6;
            margin-bottom: 1.2rem;
        }

        .social-links a {
            text-decoration: none;
            margin-right: 15px;
            font-size: 26px;
            color: #1a2a44;
            transition: 0.3s;
        }

        .social-links a:hover {
            color: #b08968;
        }

        .profile {
            width: 260px;
            height: 260px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #1a2a44;
            box-shadow: 0 0 25px rgba(26,42,68,0.15);
        }

        /* Seções */
        .section {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            margin: 0 auto 2rem auto;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
            max-width: 1000px;
        }

        .section h2 {
            color: #1a2a44;
            border-left: 6px solid #b08968;
            padding-left: 10px;
            margin-bottom: 15px;
        }

        .section ul {
            list-style-type: disc;
            margin-left: 20px;
            line-height: 1.6;
        }

        .button {
            display: inline-block;
            background-color: #1a2a44;
            color: white;
            padding: 0.6em 1.4em;
            border-radius: 8px;
            text-decoration: none;
            transition: 0.3s;
            font-weight: 600;
        }

        .button:hover {
            background-color: #2e4775;
        }

        .footer {
            text-align: center;
            color: #777;
            margin-top: 3rem;
            margin-bottom: 1rem;
            font-size: 14px;
        }

        /* Ajuste responsivo */
        @media (max-width: 900px) {
            .header-container {
                flex-direction: column-reverse;
                text-align: center;
            }
            .header-text {
                padding-right: 0;
            }
            .profile {
                margin-bottom: 1.5rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- CABEÇALHO (duas colunas) ----------------
col1, col2 = st.columns([3, 1])  # criar as colunas após set_page_config e CSS

with col1:
    st.markdown("""
        <div class="header-container">
            <div class="header-text">
                <h1 class="name">Mariele Coelho</h1>
                <h3 class="subtitle">Estudante de Ciências Contábeis</h3>
                <p class="intro">
                    Estudante dedicada e apaixonada por finanças e contabilidade.  
                    Busco aplicar meus conhecimentos para promover uma gestão eficiente, ética e estratégica.
                </p>
                <div class="social-links">
                    <a href='mailto:marielebcoelho@gmail.com' title='E-mail'>📧</a>
                    <a href='https://www.linkedin.com/in/marielebcoelho' target='_blank' title='LinkedIn'>💼</a>
                    <a href='https://drive.google.com/file/d/1uGQLIVyZnDlQImnqzUtW0x-xmpQYyKsz/view' target='_blank' class='button'>📄 Ver Currículo</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Ajuste width para combinar com CSS (260px) — Streamlit ajusta proporcionalmente
    st.image(imagem, width=260, caption="") 

# ---------------- SEÇÃO FORMAÇÃO ----------------
st.markdown("""
<div class='section'>
<h2>Formação Acadêmica</h2>
<ul>
    <li><strong>Ciências Contábeis</strong> — Universidade UNOPAR, 2022 - Atual</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- SEÇÃO HABILIDADES ----------------
st.markdown("""
<div class='section'>
<h2>Habilidades</h2>
<ul>
    <li>Excel avançado e planilhas financeiras</li>
    <li>Conciliação bancária e controle de caixa</li>
    <li>Rotinas contábeis e fiscais</li>
    <li>Relatórios gerenciais e demonstrações financeiras</li>
    <li>Ética profissional e trabalho em equipe</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- SEÇÃO EXPERIÊNCIAS ----------------
st.markdown("""
<div class='section'>
<h2>Experiências</h2>
<p><strong>Acessora</strong> — Administração Regional do Itapoã-DF (2024 - Atual)</p>
<ul>
    <li>Elaboração e encaminhamento de documentos oficiais, como ofícios e despachos</li>
    <li>Organização de documentos e apoio na apuração de impostos</li>
    <li>Integração entre setores de gestão, comunicação e atendimento</li>
    <li>Produção de conteúdo institucional e apoio em eventos públicos</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- SEÇÃO PROJETOS ----------------
st.markdown("""
<div class='section'>
<h2>Projetos Acadêmicos</h2>
<p><strong>1. Planejamento Tributário de Pequenas Empresas</strong><br>
Estudo desenvolvido na disciplina de Contabilidade Tributária, com foco em estratégias de redução legal da carga fiscal.</p>

<p><strong>2. Análise de Custos e Precificação</strong><br>
Simulação de tomada de decisão baseada em custos fixos e variáveis em um ambiente empresarial fictício.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- RODAPÉ ----------------
st.markdown("""
<div class='footer'>
© 2025 Mariele Coelho — Portfólio Contábil
</div>
""", unsafe_allow_html=True)
