import functools

class Retangle:
    def __init__(self, x, y) -> None:
        self.__y = y
        self.__x = x
        self.__area = None

    @staticmethod
    def calc_area(func):
        @functools.wraps(func)
        def execute(self):
            self.__area = self.__y * self.__x
            print(self.__area)
            return func(self)
        
        return execute

    @property
    def get_area(self):
        return self.__area
    
    @get_area.setter
    def get_area(self, x):
        self.__area = x

    @calc_area
    def area(self):
        print("#" * 40)
        print(f"O valor da area e {self.__area}")

def main():    
    instance = Retangle(x=10, y=9)
    instance.area()

if __name__ == "__main__":
    main()