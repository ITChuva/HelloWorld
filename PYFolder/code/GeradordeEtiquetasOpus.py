import threading
import requests
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import json
import os
from openpyxl import Workbook

def requisicao_consulta_nf(nCodNF, nNF):
    url_nf = "https://app.omie.com.br/api/v1/produtos/nfconsultar/"
    dados_nf = {
        "call": "ConsultarNF",
        "app_key": "1826443506888",
        "app_secret": "c9e60167e96e156e2655a92fdcd77df7",
        "param": [
            {
                "nCodNF": nCodNF,
                "nNF": nNF
            }
        ]
    }
    response = requests.post(url_nf, json=dados_nf)

    if response.status_code == 200:
        resposta_json = response.json()
        
        nf_dest = resposta_json.get("nfDestInt", {})
        razao_social_dest = nf_dest.get("cRazao", "")
        cnpj_cpf_dest = nf_dest.get("cnpj_cpf", "")
        nCodCli = nf_dest.get("nCodCli", "")

        ide = resposta_json.get("ide", {})
        numero_nf_dest = ide.get("nNF", "")
        tp_nf = ide.get("tpNF", "")

        detalhes_produtos = []
        detalhes = resposta_json.get("det", [])
        for detalhe in detalhes:
            prod = detalhe.get("prod", {})
            cProd = prod.get("cProd", "")
            xProd = prod.get("xProd", "")
            vProd = prod.get("vProd", "")
            qCom = prod.get("qCom", "")
            detalhes_produtos.append({"cProd": cProd, "xProd": xProd, "vProd": vProd, "qCom": qCom})

        nf_emit_int = resposta_json.get("nfEmitInt", {})
        nCodEmp = nf_emit_int.get("nCodEmp", "")

        return razao_social_dest, cnpj_cpf_dest, numero_nf_dest, tp_nf, detalhes_produtos, nCodEmp, nCodCli
    else:
        print("Erro na requisição. Código de status:", response.status_code)
        print(response.text)
        return None, None, None, None, None, None, None

def requisicao_consultar_empresa(nCodEmp):
    url = "https://app.omie.com.br/api/v1/geral/empresas/"
    dados = {
        "call": "ConsultarEmpresa",
        "app_key": "1826443506888",
        "app_secret": "c9e60167e96e156e2655a92fdcd77df7",
        "param": [
            {
                "codigo_empresa": nCodEmp
            }
        ]
    }
    response = requests.post(url, json=dados)

    if response.status_code == 200:
        dados_empresa = response.json()
        return {
            'razao_social': dados_empresa.get('razao_social', ''),
            'telefone1_ddd': dados_empresa.get('telefone1_ddd', ''),
            'telefone1_numero': dados_empresa.get('telefone1_numero', '')
        }
    else:
        print("Erro na requisição:", response.status_code)
        return None

def requisicao_consulta_endereco_dest(nCodCli):
    app_key = "1826443506888"
    app_secret = "c9e60167e96e156e2655a92fdcd77df7"
    url = "https://app.omie.com.br/api/v1/geral/clientes/"
    dados = {
        "call": "ConsultarCliente",
        "app_key": app_key,
        "app_secret": app_secret,
        "param": [
            {
                "codigo_cliente_omie": nCodCli,
                "codigo_cliente_integracao": ""
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(dados), headers=headers)

    if response.status_code == 200:
        resposta_json = response.json()
        endereco = resposta_json.get('endereco', '')
        endereco_numero = resposta_json.get('endereco_numero', '')
        bairro = resposta_json.get('bairro', '')
        cidade = resposta_json.get('cidade', '')
        estado = resposta_json.get('estado', '')
        complemento = resposta_json.get('complemento', '')
        cep = resposta_json.get('cep', '')
        endereco_completo = f"{endereco}, {endereco_numero}, {bairro}, {cidade}, {estado}, {complemento}, {cep}"
        return endereco_completo
    else:
        print("Erro na requisição. Código de status:", response.status_code)
        print(response.text)
        return None

def consultar_nf():
    nNF = entry_nf.get()
    resultado_nf = requisicao_consulta_nf("0", nNF)
    if resultado_nf:
        razao_social_dest, cnpj_cpf_dest, numero_nf_dest, tp_nf, detalhes_produtos, nCodEmp, nCodCli = resultado_nf
        info_nf_label.config(text=f"Razão Social (dest): {razao_social_dest}\nCNPJ/CPF (dest): {cnpj_cpf_dest}\nNúmero NF (dest): {numero_nf_dest}\nTipo NF: {tp_nf}\n")
        
        produtos_info = ""
        for idx, detalhe in enumerate(detalhes_produtos, start=1):
            produtos_info += f"Produto {idx}:\nCódigo do Produto: {detalhe['cProd']}\nDescrição: {detalhe['xProd']}\nValor do Produto: {detalhe['vProd']}\nQuantidade: {detalhe['qCom']}\n\n"
        
        produtos_nf_label.config(text=produtos_info)
        
        threading.Thread(target=consultar_empresa_endereco, args=(nCodEmp, nCodCli, resultado_nf)).start()

def consultar_empresa_endereco(nCodEmp, nCodCli, resultado_nf):
    dados_empresa = requisicao_consultar_empresa(nCodEmp)
    if dados_empresa:
        empresa_info_label.config(text=f"Razão Social: {dados_empresa['razao_social']}\nTelefone: ({dados_empresa['telefone1_ddd']}) {dados_empresa['telefone1_numero']}")
            
        endereco_dest = requisicao_consulta_endereco_dest(nCodCli)
        if endereco_dest:
            threading.Thread(target=gerar_planilha_excel, args=(resultado_nf, dados_empresa, endereco_dest)).start()

def gerar_planilha_excel(resultado_nf, dados_empresa, endereco_dest):
    razao_social_dest, cnpj_cpf_dest, numero_nf_dest, tp_nf, detalhes_produtos, _, _ = resultado_nf
    
    # Criar um novo Workbook
    wb = Workbook()
    ws = wb.active

    # Definir os cabeçalhos da planilha
    ws.append(["Nota Fiscal", "Remetente", "Destinatário", "CNPJ/CPF Destinatário", "Endereço Destinatário", "Descrição Produto", "Código Produto", "Quantidade", "Valor Produto"])

    # Adicionar dados na planilha
    for produto in detalhes_produtos:
        ws.append([
            numero_nf_dest,
            dados_empresa['razao_social'],
            razao_social_dest,
            cnpj_cpf_dest,
            endereco_dest,
            produto['xProd'],
            produto['cProd'],
            produto['qCom'],
            produto['vProd']
        ])

    # Salvar o arquivo no diretório onde o app está sendo executado
    excel_filename = f"plan_{numero_nf_dest}.xlsx"
    diretorio_atual = os.getcwd()  # Diretório atual onde o app está rodando
    caminho_arquivo = os.path.join(diretorio_atual, excel_filename)
    wb.save(caminho_arquivo)
    print(f"Planilha salva em: {caminho_arquivo}")


