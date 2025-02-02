import dis
class A:
    static_v="abc"#static variables
    def __init__(self):
        self._static_vari=30
        
    def display_info(self):
        print("the static variable is:",self._static_vari)
        
obj=A()
print(obj.static_v)
obj.display_info()
static_v="vbc"
print(obj.static_v)
#dis.dis(A)