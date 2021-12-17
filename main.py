# Validador de Cpf/Cnpj/CNH

# imports
from validate_docbr import CPF, CNPJ, CNH


class Documento:

    @staticmethod
    def cria_documento(documento, tipo_documento):
        if tipo_documento == 'cpf':
            return DocCpf(documento)

        elif tipo_documento == 'cnpj':
            return DocCnpj(documento)
        elif tipo_documento == 'cnh':
            return DocCnh(documento)
        else:
            raise ValueError('Quantidade de digitos inválida!')


class DocCpf:

    def __init__(self, documento):
        if self.valida_doc(documento):
            self.cpf = documento
        else:
            raise ValueError('Cpf Inválido')

    # imprime o número do cpf formatado
    def __str__(self):
        return self.format_cpf()

    # Validação do CPF
    def valida_doc(self, documento):
        doc_cpf = CPF()
        return doc_cpf.validate(documento)

    # formatação do cpf
    def format_cpf(self):
        doc_cpf = CPF()
        return doc_cpf.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):

        if self.valida_doc(documento):
            self.cnpj = documento
        else:
            raise ValueError('Cnpj inválido')

    def __str__(self):
        return self.format_cnpj()

    # Validação do CNPJ
    def valida_doc(self, documento):
        doc_cnpj = CNPJ()
        return doc_cnpj.validate(documento)

    # Retorna o CNPJ formatado
    def format_cnpj(self):
        doc_cnpj = CNPJ()
        return doc_cnpj.mask(self.cnpj)


class DocCnh:

    def __init__(self, documento):
        if self.valida_doc(documento):
            self.cnh = documento
        else:
            raise ValueError('Número inválido')

    def __str__(self):
        return self.format_cnh()

    # Validação da CNH
    def valida_doc(self, documento):
        doc_cnh = CNH()
        return doc_cnh.validate(documento)

    # Retorna a CNH formatada
    def format_cnh(self):
        doc_cnh = CNH()
        return doc_cnh.mask(self.cnh)



objeto = Documento.cria_documento('96878921916', 'cnh')
print(objeto)
