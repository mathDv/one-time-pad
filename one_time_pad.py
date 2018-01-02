# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import binascii
from binascii import hexlify
from binascii import unhexlify
#import array
__author__ = "mdv"
__date__ = "$Apr 14, 2016 2:53:32 PM$"

if __name__ == "__main__":
    ###########################################################################
    print "Trabalho 2 - ONE TIME PAD"
    print "Autor - Matheus Duarte Vasconcelos"
    print "DISCIPLINA DE CRIPTOGRAFIA\n"
    ###########################################################################

    ###########################################################################
    ##declara mensagens codificadas hard code
    a = "3939252352554c5f51592621294d5c5229382f5d454b485d4554413132275458482d3157415046495c5b2a435a46543527364d5059394847382a2b4b555746404a38202d4c525652455c2a"
    b = "4d514c503134405f305f4e44292c41534a57414f2c2c2d4054544d5f552741424c5931345f415d2c2e4d4454405e504142522e31424a434c5f2a2b415a412f585a55452d2e20394941562a"
    c = "56574023455d4449305b4745295b5b5a45385f59435a44574526453132445c5a454843404d585a2c4146464e3246544146554531445c49574a435f573a"
    d = "505725575951292c53594f515d435544484847522c2c4e5f4155575441274c45582d465d444c2e404b495859324f4f4227424131545644444d594e2e554a4b2c4757204947465f4c53572a"
    e = "4d5625565f504c5e435f474f4d2c565f5a5b5d4e58492d4352494650504e59435954315d5b2047415e4758435349543553592e44595d4f504b5e4a4050244c5e4a48544249525849484b2a"
    f = "5c57424f5847412c5c4e52554c5e41364f4a4a5a594943505926455d5e4842592d545e412854412c4c5a4f565927565c40534054455c2a43564e2b4d55415c4d413843445e485c4b533c"
    g = "5a4b5c53455b4e5e515b4e5829454136594a4a584942593349482442575150584c413150414648495c4d44433253594542452e5e51394b524846424d555046435d4b20434157585d414b5722"
    h = "505f255a5e41294a5f5e484529585a532957414e2c58445e45265450562b355e45485f34514f5b2c46495c523241495b4e45465453395e4a51592b2e574b5a5e405d57425c4b37"
    i = "5c6f607168346a607f7e6221616d613668387c62607a6861206a6d7f7b697224"
    #copia strngs
    s1 = a
    s2 = b
    s3 = c
    s4 = d
    s5 = e
    s6 = f
    s7 = g
    s8 = h
    s9 = i
    print "--------------------------------------------------------------------"
    print "--------------------------------------------------------------------"
    ############################################################################
    #mostras mensagem em ascii e hex
    print "Cipher text 1"
    print "ascii: ", binascii.unhexlify(a) 
    print "hex  : ", a 
    print "\n"
    print "Cipher text 2"
    print "ascii: ", binascii.unhexlify(b) 
    print "hex  : ", b 
    print "\n"
    print "Cipher text 3"
    print "ascii: ", binascii.unhexlify(c) 
    print "hex  : ", c 
    print "\n"
    print "Cipher text 4"
    print "ascii: ", binascii.unhexlify(d) 
    print "hex  : ", d 
    print "\n"
    print "Cipher text 5"
    print "ascii: ", binascii.unhexlify(e) 
    print "hex  : ", e 
    print "\n"
    print "Cipher text 6"
    print "ascii: ", binascii.unhexlify(f) 
    print "hex  : ", f 
    print "\n"
    print "Cipher text 7"
    print "ascii: ", binascii.unhexlify(g) 
    print "hex  : ", g 
    print "\n"
    print "Cipher text 8"
    print "ascii: ", binascii.unhexlify(h) 
    print "hex  : ", h 
    print "\n"
    print "Cipher text 9"
    print "ascii: ", binascii.unhexlify(i) 
    print "hex  : ", i 
    print "\n"
        
    ############################################################################
    #Brief - Comparar mensgem 1 com todas as outras mensagens - ideia e que
#            apareca algum texto que faca sentido, e a partir dai deduzir outros caracteres da chave
    print "--------------------------------------------------------------------"
    print "--------------------------------------------------------------------"
    print "XOR mensagem 1 x n"
    arrayLine = []
    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s2):]), unhexlify(s2))))
    print "XOR s1 e s2: ", (arrayLine)
    print "XOR s1 e s2: ", binascii.unhexlify(arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s3):]), unhexlify(s3))))
    print "XOR s1 e s3: ", (arrayLine)
    print "XOR s1 e s3: ", binascii.unhexlify(arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s4):]), unhexlify(s4))))
    print "XOR s1 e s4: ", binascii.unhexlify(arrayLine)
    print "XOR s1 e s4: ", (arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s5):]), unhexlify(s5))))
    print "XOR s1 e s5: ", binascii.unhexlify(arrayLine)
    print "XOR s1 e s5: ", (arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s6):]), unhexlify(s6))))
    print "XOR s1 e s6: ", binascii.unhexlify(arrayLine)
    print "XOR s1 e s6: ", (arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s7):]), unhexlify(s7))))
    print "XOR s1 e s7: ", binascii.unhexlify(arrayLine)
    print "XOR s1 e s7: ", (arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s8):]), unhexlify(s8))))
    print "XOR s1 e s8: ", binascii.unhexlify(arrayLine)
    print "XOR s1 e s8: ", (arrayLine)
    print "\n"

    arrayLine = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s9):]), unhexlify(s9))))
    print "XOR s1 e s9: ", binascii.unhexlify(arrayLine)
    print "XOR s1 e s9: ", (arrayLine)
    print "\n"    
    ###########################################################################
    print "--------------------------------------------------------------------"
    print "--------------------------------------------------------------------"
    print "Show Keys"
#    historico da deducao da chave
#    probKey = "393925233134290c" ok
#    probKey = "393925233134290c302b26" 
#    probKey = "393925233134290c302b2621092c323629382f2b0c" #inicio vigenere
#    probKey = "393925233134290c302b2621092c323629382f2b0c2c2d3320262411" OK - fim vigenere
#    probKey = "393925233134290c302b2621092c323629382f2b0c2c2d332026241132"
#    probKey = "393925233134290c302b2621092c323629382f2b0c2c2d332026241115001c" - funcionou para ultima mensagem
#    probKey = "393925233134290c302b2621092c323629382f2b0c2c2d3320262411" - ok ate strin = mensagem 2
#    probKey = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d31342820" - OK will msg 4
#    probKey = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338" - ok ate tim mensagem 2
#    probKey =     "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338200d0e004928"-teste naok

#   Brief - coloquei no codigo varias chaves para ficar correto com o fim dos 
#           textos, inserindo um ponto final, pois as mensagns tinham tamanho diferene.
    probKey =     "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338200d0e203939203204"
    #chave mensgem 1
    probKeyMsg1 = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338200d0e203939203204"
    ##chave da mensagem 3 - ok
    probKeyMsg3 = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e14"
    #chave da mensagem 6 - ok
    probKeyMsg6 = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338200d0e2039392012"
    #chave da mensagem 7 - ok
    probKeyMsg7 = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338200d0e2039392032240c"
    ##chave da mensagem 8 - ok
    probKeyMsg8 = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207152a2d2d313428202e2c2e280a373227203527362e3137390a22382a2b2e34042f2c3338200d0e0019"
    ##chave da mensagem 9 - menor tamanho - ok
    probKeyMsg9 = "393925233134290c302b2621092c323629382f2b0c2c2d33202624113207150a"
    ###########################################################################
#    print "Key 1     ", binascii.unhexlify(probKeyMsg1) 
    print "Key 1     ", probKeyMsg1
    print "--------------------------------------------------------------------"
#    print "Key 3     ", binascii.unhexlify(probKeyMsg3) 
    print "Key 3     ", probKeyMsg3
    print "--------------------------------------------------------------------"
#    print "Key 2,4,5 ", binascii.unhexlify(probKey) 
    print "Key 2,4,5 ", probKey
    print "--------------------------------------------------------------------"
#    print "Key 6     ", binascii.unhexlify(probKeyMsg6) 
    print "Key 6     ", probKeyMsg6
    print "--------------------------------------------------------------------"
#    print "Key 7     ", binascii.unhexlify(probKeyMsg7) 
    print "Key 7     ", probKeyMsg7
    print "--------------------------------------------------------------------"
#    print "Key 8     ", binascii.unhexlify(probKeyMsg8) 
    print "Key 8     ", probKeyMsg8
    print "--------------------------------------------------------------------"
#    print "Key 9     ", binascii.unhexlify(probKeyMsg9) 
    print "Key 9     ", probKeyMsg9
    print "--------------------------------------------------------------------"
    print "--------------------------------------------------------------------"
    ###########################################################################
    print "Show plain txt"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKeyMsg1[-len(a):]), unhexlify(a))))
    print "Msg1: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKey[-len(b):]), unhexlify(b))))
    print "Msg2: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKeyMsg3[-len(c):]), unhexlify(c))))
    print "Msg3: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKey[-len(d):]), unhexlify(d))))
    print "Msg4: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKey[-len(e):]), unhexlify(e))))
    print "Msg5: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKeyMsg6[-len(f):]), unhexlify(f))))
    print "Msg6: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKeyMsg7[-len(g):]), unhexlify(g))))
    print "Msg7: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKeyMsg8[-len(h):]), unhexlify(h))))
    print "Msg8: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    msg2 = hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(probKeyMsg9[-len(i):]), unhexlify(i))))
    print "Msg9: ", binascii.unhexlify(msg2)
    print "--------------------------------------------------------------------"
    print "------------------------END OF PROGRAM------------------------------"