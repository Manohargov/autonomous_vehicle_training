class parent_cls:
    def a(self):
        print("hello form a")
class child_cls(parent_cls):
    def b(self):
        print("hello form b")
class grandchild_cls(child_cls):
    def c(self):
         print("helo form c")
        
obj_gc =grandchild_cls()
obj_gc.a()
obj_gc.b()
obj_gc.c()
