class Sal:
    min_wage = 9860
    def __init__(self, basic, night):
        self.basic = basic
        self.night = night
        self._sal = self.basic * self.min_wage + self.night * (self.min_wage * 1.5)
        self._tax = self._sal * 0.033

    def getSal(self):
        return self._sal
    def getTax(self):
        return self._tax
    def getRec(self):
        return self._sal - self._tax
    


basic_time = int(input("기본 시급 일한 시간 입력 : "))
night_time = int(input("야간 일한 시간 입력 : "))

sal_instance = Sal(basic_time, night_time)
print("월급 : ", sal_instance.getSal())
print("3.3% 세금 : ", sal_instance.getTax())
print("실 수령액 : ", sal_instance.getRec())