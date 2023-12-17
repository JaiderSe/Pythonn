class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub( Right,Left):##si cambiamos el resultado de estas clases el resultado sera distinto
    pass


obj = Sub()

print(obj.var,obj.var, obj.var_left, obj.var_right, obj.fun())
    