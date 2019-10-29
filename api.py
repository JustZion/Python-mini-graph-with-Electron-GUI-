from graphpot import main_p 
import time
import sys
import zerorpc

class CalcApi(object):
    def calc(self, a,b,c):
        """based on the input text, return the int result"""
        try:
            a = int(a)
        except:
            return "Please Enter a Valid Input For x"
        try:
            b = int(b)
        except:
            return "Please Select a Proper Option"
        try:
            c = int(c)
            return main_p(a,b,c)
            
        except:
            return "Please Select a Proper Option"

    

def main():
    addr = 'tcp://127.0.0.1:' + '4242'
    s = zerorpc.Server(CalcApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()