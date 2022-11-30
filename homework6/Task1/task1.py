# ==== Расчет нормативного расхода топлива на отопление здания ====


class specThermalChar:
    # расчет удельной тепловой характеристики здания

    def __init__(self, V, F_build, F_wall, F_win):
        # Геометрические характеристики здания:
        self.V = V # объем
        self.F_build = F_build # площадь здания
        self.F_wall = F_wall # площадь стен
        self.F_win = F_win # площадь окон

    def d_glazing(self):
        # расчет доли остекления
        d = self.F_win / self.F_wall
        return d

    def q_char(self):
        # расчет удельной тепловой характеристики здания
        q = ((1 + 2 * self.d_glazing()) * self.F_wall + self.F_build) / self.V
        return q


class thermLoad(specThermalChar):
    # Расчет тепловой нагрузки здания

    def __init__(self, V, F_build, F_wall, F_win, tvn, trnv, N, tsrn):
        specThermalChar.__init__(self, V, F_build, F_wall, F_win)

        # Климатические данные
        self.tvn = tvn # температура внутри помещения
        self.trnv = trnv # расчетная температура наружного воздуха
        self.N = N # продолжительность отопительного периода
        self.tsrn = tsrn  # редняя температура наружного воздуха за отопительный период

    def Qmax(self):
        Q = specThermalChar.q_char(self) * self.V * (self.tvn - self.trnv) / 1000000
        return Q


class boilerEfficiency:
    # Удельный расход топлива котлом
    def __init__(self, kpd):
        # КПД котла
        self.kpd = kpd

    def b_boiler(self):
        # расчет удельного расхода
        b = 14286 / self.kpd
        return b


class fuelConsumption:
    # расчет расхода топлива
    def __init__(self, Qmax, b, tvn, trnv, N, tsrn):
        self.Qmax = Qmax
        self.b = b
        self.tvn = tvn
        self.trnv = trnv
        self.N = N
        self.tsrn = tsrn

    def B_fuel(self):
        B = self.Qmax * ((self.tvn - self.tsrn) / (self.tvn - self.trnv)) * self.N * 24 * self.b / 1000
        return B


def calculation_fuel(V, F_build, F_wall, F_win, tvn, trnv, N, tsrn, kpd):
    #Вывод результата

    Qmax_calc = thermLoad(V, F_build, F_wall, F_win, tvn, trnv, N, tsrn)

    b_calc = boilerEfficiency(kpd)

    B_calc = fuelConsumption(Qmax_calc.Qmax(), b_calc.b_boiler(), Qmax_calc.tvn,
                             Qmax_calc.trnv, Qmax_calc.N, Qmax_calc.tsrn)

    B = round(B_calc.B_fuel(), 2)

    return print(f"Расход топлива на отопление здания равен: {B} т у.т")



def input_temp(a):
    # проверка ввода данных
    while True:
        try:
            a = float(a.replace(',', '.'))
        except ValueError:
            print("-== Неверный ввод данных ==-")
            a = input("Повторите ввод данных:  ")
            continue
        else:
            return a


# class KpdError(ValueError):
#     pass
#
# def input_kpd(a):
#     # проверка ввода данных КПД котла
#     while True:
#         try:
#             a = float(a.replace(',', '.'))
#         except ValueError:
#             print("-== Неверный ввод данных ==-")
#             a = input("Повторите ввод данных:  ")
#             continue
#         else:
#             return a
#     try:
#         a > 100



def data_entry():
    #Ввод данных
    data_fuel = []

    data_fuel.append(input_temp(input("Введите объем здания, м3: ")))
    data_fuel.append(input_temp(input("Введите площадь здания, м2: ")))
    data_fuel.append(input_temp(input("Введите площадь стен здания, м2: ")))
    data_fuel.append(input_temp(input("Введите площадь окон, м2: ")))
    data_fuel.append(input_temp(input("Введите температуру внутри помещения, С: ")))
    data_fuel.append(input_temp(input("Введите расчетную температуру наружного воздуха, С: ")))
    data_fuel.append(input_temp(input("Введите продолжительность отопительного периода, сут.: ")))
    data_fuel.append(input_temp(input("Введите среднюю температуру наружного воздуха за отопительный период, С: ")))
    data_fuel.append(input_temp(input("Введите КПД котла, %: ")))

    calculation_fuel(*data_fuel)

data_entry()


# calculation_fuel(190, 43, 102.37, 9, 18, -24, 188, -1, 75)
# результат 2.67 т у.т















# # (V, F_build, F_wall, F_win)
# rezult_fuel = specThermalChar(190, 43, 102.37, 9)
# print(rezult_fuel.ThermalChar())
# # (tvn, trnv, N, tsrn, V, F_build, F_wall, F_win)
# temp = thermLoad(190, 43, 102.37, 9, 18, -24, 188, -1)
# print(temp.Qmax())
# kpd = boilerEfficiency(75)
# print(kpd.kpd_boiler())



