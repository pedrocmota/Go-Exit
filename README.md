# Go Exit

Esse é um programa que deveria ser nativo do Windows, porém não é. 
Sabe quando você fica preso em uma tela na qual não consegue sair, nem mesmo pelo gerenciador de tarefas?

Então, esse software resolve esse problema, basta usar um único atalho que, em um passe de mágica, o programa focado será 
finalizado instantaneamente.

Note que essa funcionalidade difere do famoso alt+f4, visto o Go Exit finaliza o processo, diferente de outros métodos nativos.

### Instalação

Basta baixar o executável no Github e executá-lo. É obrigatório rodar esse programa com root, visto que esse acessa algumas API's do Windows.

O software perguntará se você deseja que ele execute a cada inicialização, caso positivo, uma tarefa será criada no Task Scheduler com o caminho atual do executável.

### Uso e configurações

Com o Go Exit em execução, basta usar o atalho em uma janela focada, que o processo correspondente será finalizado instantaneamente.

O arquivo de configurações do Go Exit pode ser aberto pela bandeja, ou então acessado diretamente pelo caminho:

```console
%APPDATA%\goexit\configs.json
```

A estrutura do arquivo de configurações é:

```javascript
{
  "shortcut": "<cmd_l>+<alt>+c",
  "exclude": [
    "explorer.exe"
  ]
}
```

*Shortcut*: Atalho para finalizar o processo, o padrão é

```console
Win + alt + c
```

Exclude: Array de processo sempre ignorados pelo atalho, por padrão o explorer.exe é invisível ao finalizador
para evitar danificar o seu sistema, mantenha-o assim.

Para que as alterações tenham efeito, é necessário reiniciar o Go Exit.

### Desenvolvimento

Para rodar o Go Exit em desenvolvimento, primeiro você precisa do Python 3.
Depois instale as dependências com o seguinte código:

```console
pip install -r requirements.txt
```

E por último, roda o arquivo "index.py"

```console
python index.py
```

Nota: O python deverá rodar no modo root, caso contrário, o software não irá funcionar.

### Licença

[MIT](https://choosealicense.com/licenses/mit/), fique livre para modificar