##### method / classmethod / staticmethod

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x
x="abc"
a=A()
a.foo(x)

##### % and format
# x=("abc", 1)
a.static_foo(x)
# print map("hello {0}".format, x)

a.class_foo(x)
##### 



MAXIMUM_VALUE = 10

class Animal:
    cache = {}
    def run(self, n):
        if n in self.cache:
            print 'cache', self.cache
            return self.cache[n]

        if n == MAXIMUM_VALUE:
            # self.cache = {}
            self.cache.clear()

        result = 2 ** n
        self.cache[n] = result
        return result

bird = Animal()
print bird.run(2)
print bird.run(3)
print bird.run(2)
print bird.run(10)
print bird.run(2)
print bird.run(2)

