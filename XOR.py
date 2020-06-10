__author__ == 'Michael Y'



class Xor:
    def __init__(self, variant, cText):
        self.variant = variant
        self.cText = cText
        if len(cText) != 32:
            raise ValueError("Invalid Key Length. Your key is {} {} character(s) from the required length.".
                             format(">" if len(cText) < 0 else "<", len(cText)-32))

    def splitFoo(self):
        return self.cText[:16]

    def splitBar(self):
        return self.cText[16:]

    def XorFirstHalf(self):
        return '%x' % (int(self.splitFoo(), 16) ^ int(self.variant, 16))

    def XorSecondHalf(self):
        return '%x' % (int(self.splitBar(), 16) ^ int(self.variant, 16))

    def clearKey(self):
        return str(self.XorFirstHalf()+self.XorSecondHalf())
        
    
 #  x = Xor(Foo, Bar)
