class first_class:
    def add(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)


class second_class:
    def mul(self,a,b):
        print(a*b)

    def div(self,a,b):
        print(a/b)
        

obj_1= first_class()
obj_1.add(10,20)
obj_1.sub(10,20)

obj_2= second_class()
obj_2.mul(10,20)
obj_2.div(10,20)
