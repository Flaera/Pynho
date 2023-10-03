

class Types():
    def __init__(self):
        '''Constructor of classes of word in compiler/interpretator.'''
        self.PR = [
            "if", "then", "else",
            "int", "real", "boolean",
            "print", "f",
            "return", "function",
            "write", "read",
            "for", "while",
            
            "programa_SOL", "sequencia", "tempo", "fases_EPIC",
            "Explore", "Interact", "Present", "Critique",
            "navegar", "browser",
            "visualizar_pdf", "visualizar_video", "videoconferencia",
            "whatsapp_web", "email"
        ]

        self.TIME = ["30_min", "1_hora", "1_dia", "2_dias", "sem_limite"]
        
        self.DS = [";",".",",","(",")","[","]"]
        
        self.DC = ["begin", "end"]

        self.MATH_OPERATORS = ["+","-","*","/","="]

        self.REL_OPERATORS = ["==",">","<",">=","<=","!"]

        self.VALUES_BOLLEAN = ["true", "false", "empty"]

        self.DIGIT = ["0","1","2","3","4","5","6","7","8","9"]


class AnaliserLexic():
    def __init__(self, _input_data):
        self.input_data = _input_data
        self.acc_tokens = int(0)
        self.tokens = []
        self.types = Types()


    def AddPRToken(self, part, index):
        if (part.find(self.types.PR[index])==0):
            self.tokens.append([self.types.PR[index], "WORD_RESERVED", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0


    def AddTIMEToken(self, part, index):
        if (part.find(self.types.TIME[index])>-1):
            self.tokens.append([self.types.TIME[index], "TIME", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0
    

    def AddDSToken(self, part, index):
        if (part.find(self.types.DS[index])>-1):
            self.tokens.append([self.types.DS[index], "DELIMITER_SIMPLE", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0


    def AddDCToken(self, part, index):
        if (part.find(self.types.DC[index])>-1):
            self.tokens.append([self.types.DC[index], "DELIMITER_COMPOST", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0


    def AddMOToken(self, part, index):
        if (part.find(self.types.MATH_OPERATORS[index])>-1):
            self.tokens.append([self.types.MATH_OPERATORS[index], "MATH_OPERATOR", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0
    

    def AddROToken(self, part, index):
        if (part.find(self.types.REL_OPERATORS[index])>-1):
            self.tokens.append([self.types.REL_OPERATORS[index], "REL_OPERATOR", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0


    def AddVBToken(self, part, index):
        if (part.find(self.types.VALUES_BOLLEAN[index])>-1):
            self.tokens.append([self.types.VALUES_BOLLEAN[index], "VALUES_BOOLEAN", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0

    
    def AddDIGITToken(self, part, index):
        if (part.find(self.types.DIGIT[index])>-1):
            self.tokens.append([self.types.DIGIT[index], "DIGIT", self.acc_tokens])
            self.acc_tokens+=1
            return 1
        return 0


    def AddERRORToken(self, part):
        self.tokens.append([part, "ERROR_LEXIC", self.acc_tokens])
        self.acc_tokens+=1


    def AddIDToken(self, part):
        part1 = part.split('(')


    def ShowTokens(self):
        print("Tokens finded:")
        for m in range(0,len(self.tokens)):
            print(f"Token value={self.tokens[m][0]} | {self.tokens[m][1]} | {self.tokens[m][2]}")


    def Run(self):
        print("Tokenzing process initializated...")
        parts = []
        res = []
        part1 = []
        for i in self.input_data:
            part1 = i.split(" ")
            for j in part1:
                parts.append(j)
        print("parts=",parts)
        for k in parts:
            # print("k=",k,"")
            
            res.append(self.AddPRToken(k,0))
            res.append(self.AddPRToken(k,1))
            res.append(self.AddPRToken(k,2))
            res.append(self.AddPRToken(k,3))
            res.append(self.AddPRToken(k,4))
            res.append(self.AddPRToken(k,5))
            res.append(self.AddPRToken(k,6))
            res.append(self.AddPRToken(k,7))
            res.append(self.AddPRToken(k,8))
            res.append(self.AddPRToken(k,9))
            res.append(self.AddPRToken(k,10))
            res.append(self.AddPRToken(k,11))
            res.append(self.AddPRToken(k,12))
            res.append(self.AddPRToken(k,13))
            res.append(self.AddPRToken(k,14))
            res.append(self.AddPRToken(k,15))
            res.append(self.AddPRToken(k,16))
            res.append(self.AddPRToken(k,17))
            res.append(self.AddPRToken(k,18))
            res.append(self.AddPRToken(k,19))
            res.append(self.AddPRToken(k,20))
            res.append(self.AddPRToken(k,21))
            res.append(self.AddPRToken(k,22))
            res.append(self.AddPRToken(k,23))
            res.append(self.AddPRToken(k,24))
            res.append(self.AddPRToken(k,25))
            res.append(self.AddPRToken(k,26))
            res.append(self.AddPRToken(k,27))
            res.append(self.AddPRToken(k,28))

            res.append(self.AddTIMEToken(k, 0))
            res.append(self.AddTIMEToken(k, 1))
            res.append(self.AddTIMEToken(k, 2))
            res.append(self.AddTIMEToken(k, 3))
            res.append(self.AddTIMEToken(k, 4))

            res.append(self.AddDSToken(k, 0))
            res.append(self.AddDSToken(k, 1))
            res.append(self.AddDSToken(k, 2))
            res.append(self.AddDSToken(k, 3))
            res.append(self.AddDSToken(k, 4))
            res.append(self.AddDSToken(k, 5))
            res.append(self.AddDSToken(k, 6))

            res.append(self.AddDCToken(k,0))
            res.append(self.AddDCToken(k,1))

            res.append(self.AddMOToken(k, 0))
            res.append(self.AddMOToken(k, 1))
            res.append(self.AddMOToken(k, 2))
            res.append(self.AddMOToken(k, 3))
            res.append(self.AddMOToken(k, 4))

            res.append(self.AddROToken(k, 0))
            res.append(self.AddROToken(k, 1))
            res.append(self.AddROToken(k, 2))
            res.append(self.AddROToken(k, 3))
            res.append(self.AddROToken(k, 4))
            res.append(self.AddROToken(k, 5))

            res.append(self.AddVBToken(k, 0))
            res.append(self.AddVBToken(k, 1))
            res.append(self.AddVBToken(k, 2))

            res.append(self.AddDIGITToken(k,0))
            res.append(self.AddDIGITToken(k,1))
            res.append(self.AddDIGITToken(k,2))
            res.append(self.AddDIGITToken(k,3))
            res.append(self.AddDIGITToken(k,4))
            res.append(self.AddDIGITToken(k,5))
            res.append(self.AddDIGITToken(k,6))
            res.append(self.AddDIGITToken(k,7))
            res.append(self.AddDIGITToken(k,8))
            res.append(self.AddDIGITToken(k,9))

            if not(1 in res):
                self.AddERRORToken(k)

        self.ShowTokens()



def main():
    lines = []
    line = "000"
    is_stop = False
    number_line = 1
    while is_stop==False:
        line = input(f"{int(number_line)}:")
        if (line!=''):
            # print("AQUI")
            if (line[0]!='/' and line[1]!='/'):
                lines.append(line)
        else:
            is_stop = True
        # print("lines=",lines)
        number_line+=1
    ana_lex = AnaliserLexic(lines)
    ana_lex.Run()


main()