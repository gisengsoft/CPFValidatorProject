# CPFValidatorProject

Projeto de validação de CPF com Azure Functions (HTTP Trigger) em Python.

## ✅ Como Executar Localmente

### 1. Pré-requisitos

- Azure Functions Core Tools  
  `npm install -g azure-functions-core-tools@4 --unsafe-perm true`
- Python 3.10+ instalado
- GitHub Codespaces (opcional)
- VSCode

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Iniciar o servidor local

```bash
func start
```

Acesse no navegador:

```
http://localhost:7071/api/CpfValidator?cpf=12345678909
```

---

### 4. Exemplo de Resposta

```json
{
  "cpf": "12345678909",
  "valido": true
}
```

---

## ☁️ Como Fazer Deploy para Azure

### 1. Login com Azure CLI:

```bash
az login
```

### 2. Publicar a Function App:

```bash
func azure functionapp publish NOME_DA_SUA_FUNCTION
```

---

## 🚀 Deploy com 1 Clique (Azure)

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.FunctionApp)

---

## 👤 Desenvolvedor

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gilson%20Inacio%20da%20Silva-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/gilsoninsilva/)  
[![GitHub](https://img.shields.io/badge/GitHub-gisengsoft-black?logo=github&style=flat-square)](https://github.com/gisengsoft)

Desenvolvido com 💻 por **Gilson Inacio da Silva**