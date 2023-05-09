import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#seleção de gráficos
gsheets_show_id = st.sidebar.radio("Selecione o Dataset", ("Matemática", "Português"))
graph1_type = st.sidebar.selectbox("Gráfico 1: Selecione o tipo de gráfico", ("Barra", "Pizza", "Dispersão", "Histograma", "Boxplot"))

gsheets_math_id = "1392993996"
gsheets_portuguese_id = "0"

show_id = gsheets_math_id if gsheets_show_id == "Matemática" else gsheets_portuguese_id

gsheets_url = 'https://docs.google.com/spreadsheets/d/1pfqNNPJrB1QFcqUm5evvDeijycnuPFDztInZvl3nOyU/edit#gid=' + show_id
@st.cache_data(ttl=120)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(gsheets_url)

#opções de viszualização do dataset
st.sidebar.subheader("Selecione o que deseja exibir")
show_dataset = st.sidebar.checkbox("Dados do Dataset")
show_dataset_description = st.sidebar.checkbox("Descrição do Dataset")

if show_dataset_description:
    st.subheader("Descrição do Dataset")

    st.markdown("""
| Column    | Description                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------|
| school    | Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)                   |
| sex       | Student's sex (binary: 'F' - female or 'M' - male)                                               |
| age       | Student's age (numeric: from 15 to 22)                                                            |
| address   | Student's home address type (binary: 'U' - urban or 'R' - rural)                                  |
| famsize   | Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)                         |
| Pstatus   | Parent's cohabitation status (binary: 'T' - living together or 'A' - apart)                       |
| Medu      | Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) |
| Fedu      | Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) |
| Mjob      | Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') |
| Fjob      | Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') |
| reason    | Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other') |
| guardian  | Student's guardian (nominal: 'mother', 'father' or 'other')                                        |
| traveltime| Home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour) |
| studytime | Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)   |
| failures  | Number of past class failures (numeric: n if 1<=n<3, else 4)                                       |
| schoolsup | Extra educational support (binary: yes or no)                                                      |
| famsup    | Family educational support (binary: yes or no)                                                     |
| paid      | Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)               |
| activities| Extra-curricular activities (binary: yes or no)                                                    |
| nursery   | Attended nursery school (binary: yes or no)                                                        |
| higher    | Wants to take higher education (binary: yes or no)                                                 |
| internet  | Internet access at home (binary: yes or no)                                                        |
| romantic  | With a romantic relationship (binary: yes or no)                                                   |
| famrel    | Quality of family relationships (numeric: from 1 - very bad to 5 - excellent)                       |
| freetime  | Free time after school (numeric: from 1 - very low to 5 - very high)                               |
| goout     | Going out with friends (numeric: from 1 - very low to 5 - very high)                               |
| Dalc      | Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)                          |
| Walc      | Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)                          |
| health    | Current health status (numeric: from 1 - very bad to 5 - very good)                                |
| absences  | Number of school absences (numeric: from 0 to 93)                                                  |
""")            

if show_dataset:
    st.subheader("Conjunto de Dados")
    st.dataframe(data)
'''
#grafico de pizza
st.subheader("Distribuição de Idade dos alunos na Escola GP")
gender_count = data['sex'].value_counts()
fig, ax = plt.subplots()
if graph1_type == "Pizza":
    ax.pie(gender_count.values, labels=gender_count.index, autopct='%1.1f%%')
    ax.set_title('Distribuição de Gênero dos Estudantes')
else:
    sns.barplot(x=gender_count.index, y=gender_count.values)
    ax.set_xlabel('Gênero')
    ax.set_ylabel('Número de Estudantes')

st.pyplot(fig)
'''
#Questão 1
#grafico de barras
st.subheader("Distribuição de Idade dos alunos na Escola GP")
age = data.loc[0:350,'age'].value_counts()
fig_age, ax_age = plt.subplots()
sns.barplot(x=age.index, y=age.values)
ax_age.set_xlabel('Idade')
ax_age.set_ylabel('Número de Estudantes da Escola GP')
#aparececr números emcima das barras
for i in ax_age.containers:
    ax_age.bar_label(i,)
st.pyplot(fig_age)

#legenda
st.subheader("Média de idade dos alunos na Escola GP")
agge = data.loc[0:348,'age'].mean()
school_mean_age = {'Media GP':agge}
st.table(school_mean_age)

#Questão 2
#grafico de pizza
st.subheader("Endereços dos alunos da escola MS")
address_count = data.loc[349:398,'address'].value_counts()
fig_address, ax_address = plt.subplots()
ax_address.pie(address_count.values, labels=address_count.index, autopct='%1.1f%%')
ax_address.set_title('Distribuição por zona Urbana e Rural')
st.pyplot(fig_address)
#legenda
st.subheader("Moda do endereço dos alunos na escola MS")
school_mode_address = data.loc[349:398,'address'].mode()
st.table(school_mode_address)

#Questão 3
#grafico de linnha
st.subheader("Tempo de viagem dos alunos da escola GP")
traveltime = data.loc[0:348,'traveltime'].value_counts()
st.line_chart(traveltime)
#legenda
st.subheader('Mediana do tempo de viagem dos alunos que estudam na escola GP')
traveltime_date = data.loc[0:348,'traveltime'].mean()
school_median_traveltime = {'GP':traveltime_date}
st.table(school_median_traveltime)

#Questão 4
#grafico de barras
st.subheader('Idade dos alnos que possuem apoio educacional extra na escola MS')
schoolsup = data.loc[349:398,['schoolsup','age']].value_counts()
fig_schoolsup,ax_schoolsup = plt.subplots()
sns.barplot(data=data,x='school',y='age',hue='schoolsup')
ax_schoolsup.set_xlabel('Apoio Educacional')
ax_schoolsup.set_ylabel('Idade')
for i in ax_schoolsup.containers:
    ax_schoolsup.bar_label(i,)
st.pyplot(fig_schoolsup)

#legenda
st.subheader('desvio padrão da idade dos alunos que têm apoio educacional extra na escola MS')
df_school_sup = pd.DataFrame(schoolsup)
st.table(df_school_sup.std())

#Questão 5
#grafico
school_median_studytime_and_Pstatus = data.loc[0:348,['Pstatus','studytime']].value_counts()
studytime = {'GP':school_median_studytime_and_Pstatus['A']}
df_studytime = pd.DataFrame(studytime)
fig_studytime, ax_studytime = plt.subplots()
sns.barplot(data=data,x='Pstatus',y='studytime',hue='school')
ax_studytime.set_xlabel('Tipo do Relacionamento Familiar')
ax_studytime.set_ylabel('Tempo de Estudo')
for i in ax_studytime.containers:
    ax_studytime.bar_label(i,)
st.pyplot(fig_studytime)
#legenda
st.subheader('Média do tempo semanal de estudo dos alunos cujos pais estão separados na escola GP')
st.table(df_studytime.mean())

#Questão 6
#grafico de barras
st.subheader('Motivo que escolheram a escola MS')
reason_count = data.loc[349:398,'reason'].value_counts()
fig_reason, ax_reason = plt.subplots()
ax_reason.pie(reason_count.values, labels=reason_count.index, autopct='%1.1f%%')
ax_reason.set_title('Distribuição por zona Urbana e Rural')
st.pyplot(fig_reason)

#legenda
st.subheader('Moda do motivo pelo qual os alunos escolheram a escola MS')
school_moda_reason = data.loc[349:398,'reason'].mode()
st.table(school_moda_reason)

#Questão 7
#grafico barras
st.subheader("Números de faltas")
absences = data.loc[0:348,'absences'].value_counts()
fig_absences, ax_absences = plt.subplots()
sns.lineplot(x=absences.index, y=absences.values)
ax_absences.set_xlabel('Números de faltas')
ax_absences.set_ylabel('Quantidade de faltas')
st.pyplot(fig_absences)
#legenda
st.subheader('Mediana do número de faltas dos alunos que frequentam a escola GP')
absences = data.loc[0:348,'absences'].median()
school_median_absences= {'absences - GP':absences}
st.table(school_median_absences)

#Questão 8
#grafico barras
st.subheader("Saúde dos alunos que frequentam atividades extracurriculares")
health = data.loc[349:389,'activities'].value_counts()
health_std = data.loc[349:398,'health'].value_counts()
school_health = {'Quality health':health}

fig_health, ax_health = plt.subplots()
sns.barplot(x=health_std, y=health)
ax_health.set_xlabel('Números de faltas')
ax_health.set_ylabel('Quantidade de faltas')
#aparececr números emcima das barras
for i in ax_health.containers:
    ax_health.bar_label(i,)
st.pyplot(fig_health)

#legenda
st.subheader('Desvio padrão do nível de saúde dos alunos que frequentam atividades extracurriculares na escola MS')
school_health_std = {'Quality health':health_std.std()}
st.table(school_health_std)

#Questão 9
#grafico de linha
activities = data.loc[0:348,'activities'].value_counts()
fig_activities,ax_activities = plt.subplots()
sns.barplot(x=activities.index,y=activities.values)
ax_activities.set_ylabel('número de alunos')
ax_activities.set_xlabel('Respostas')
#aparececr números emcima das barras
for i in ax_activities.containers:
    ax_activities.bar_label(i,)
st.pyplot(fig_activities)
#legenda
st.subheader('Número de alunos da escola GP que fazem atividades extracurriculares')
school_hours_activites = {'Hours Activities': activities['yes']}
st.table(school_hours_activites)

#Questão 10
#grafico de linha
st.subheader("Números de consumo de Alcool pelos estudantes")
dalc = data.loc[0:348,'Dalc'].value_counts()
fig_dalc, ax_dalc = plt.subplots()
sns.lineplot(x=dalc.index, y=dalc.values)
ax_dalc.set_xlabel('Quantidade de consumo na semana')
ax_dalc.set_ylabel('Números de Pessoas')
st.pyplot(fig_dalc)
#legenda
st.subheader('Moda do consumo de álcool dos alunos da escola MS durante a semana de trabalho')
dalc = data.loc[349:398,'Dalc'].mode()
school_moda_dalc = {'Consume - MS':dalc}
st.table(school_moda_dalc)
