import os

GUM_ENABLED = True

class glv:
    
    @staticmethod
    def gum_pr(level, message):
        os.system(f'gum log --time ansic --level {level} "{message}"')
        

    @staticmethod
    def dprint(message:str):
        
        if GUM_ENABLED:
            glv.gum_pr("debug",message)

        else:
            print(f"[DEBUG] {message}")

    @staticmethod
    def sprint(message:str):
        
        if GUM_ENABLED:
            glv.gum_pr("info",message)

        else:
            print(f"[INFO] {message}")

    @staticmethod
    def errprint(message:str):
        
        if GUM_ENABLED:
            glv.gum_pr("error",message)

        else:
            print(f"[ERROR] {message}")


