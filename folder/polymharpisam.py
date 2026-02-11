class parent_cls:
    def a(self):
        print("hello form a")
class child_cls():
    def a(self):
        print("hello form b")
class grandchild_cls():
    def a(self):
         print("helo form c")
        
obj_gc =grandchild_cls()
obj_gc.a()

