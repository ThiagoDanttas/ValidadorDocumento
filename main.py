# Validador de Cpf/Cnpj/CNH

# imports
from validate_docbr import CPF, CNPJ, CNH


class Validador_documento:

    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        self.tipo_documento = tipo_documento

        if self.tipo_documento == 'cpf':
            if self.valida_cpf(documento):
                self.cpf = documento
        elif self.tipo_documento == 'cnh':
            if self.valida_cnh(documento):
                self.cnh = documento
        elif self.tipo_documento == 'cnpj':
            if self.valida_cnpj(documento):
                self.cnpj = documento
        else:
            raise ValueError('Documento inválido')

    def __str__(self):
        return self.documento_format()

    def documento_format(self):
        if self.tipo_documento == 'cpf':
            doc_cpf = CPF()
            return doc_cpf.mask(self.cpf)
        elif self.tipo_documento == 'cnh':
            doc_cnh = CNH()
            return doc_cnh.mask(self.cnh)
        else:
            doc_cnpj = CNPJ()
            return doc_cnpj.mask(self.cnpj)

    # valida o documento cpf
    def valida_cpf(self, documento):
        val_cpf = CPF()
        if len(documento) == 11:
            return val_cpf.validate(documento)
        else:
            raise ValueError('Número inválido')

    # valida o documento cnh
    def valida_cnh(self, documento):
        val_cnh = CNH()
        if len(documento) == 11:
            return val_cnh.validate(documento)
        else:
            raise ValueError('Número Inválido')

    # valida o documento cnpj
    def valida_cnpj(self, documento):
        val_cnpj = CNPJ()
        if len(documento) == 14:
            return val_cnpj.validate(documento)
        else:
            raise ValueError('Número inválido')


objeto = Validador_documento(43552446000131, 'cnpj')
print(objeto)
