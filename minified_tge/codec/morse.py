_M='-.-.-.'
_L='---...'
_K='..--.-'
_J='...-..-'
_I='-.-.--'
_H='.--.-.'
_G='-.--.-'
_F='-....-'
_E='..--..'
_D='.-.-.-'
_C='--..--'
_B='.-..-.'
_A='.-.-.'
def encode(message):A={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',',':_C,'.':_D,'?':_E,'/':'-..-.','-':_F,'(':'-.--.',')':_G,'&':'.-...','@':_H,'!':_I,'$':_J,'%':_A,'=':'-...-','+':_A,'_':_K,'"':_B,'<':'.-.-','>':_B,':':_L,';':_M,' ':'/'};return''.join([A[B]for B in message.lower()])
def decode(message):A=message;B={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0',_C:',',_D:'.',_E:'?','-..-.':'/',_F:'-','-.--.':'(',_G:')','.-...':'&',_H:'@',_I:'!',_J:'$',_A:'%','-...-':'=',_A:'+',_K:'_',_B:'"','.-.-':'<',_B:'>',_L:':',_M:';','/':' '};A=A.replace(' ','/').replace('_','/');return''.join([B[A]for A in A.lower()])