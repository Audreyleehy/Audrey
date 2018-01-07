class point():
    def __init__(self,name,point):
        self.__name=name
        self.__point=point


    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_point(self):
        return self.__point

    def set_point(self,point):
        self.__point=point