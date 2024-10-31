from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# CRIANDO O DATAFRAME
df = pd.DataFrame({
    'Alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'Notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html
@app.route('/table')
def table():
    # COVERETE O DATAFRAME PARA HTML SEM COLOCÁ-LO EM UMA LISTA
    table_html = df.to_html(classes='data', index=False)  # ADICIONA CLASSE E REMOVE O ÍNDICE
    return render_template('table.html', table=table_html)  # ACESSA DIRETAMENTE A STRING HTML
if __name__ == "__main__":
    app.run(debug=True)
