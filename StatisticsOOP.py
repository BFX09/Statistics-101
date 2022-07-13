import math


class Frequency_Distribution:
    def __init__(self, array):
        self.array = array
        array.sort()
        self.n = n = len(array)
        self.x_max = round(array[-1] + float(f'0.{self.DecimalCounter()*"0"}5'), self.DecimalCounter()+1)
        self.x_min = round(array[0] - float(f'0.{self.DecimalCounter()*"0"}5'), self.DecimalCounter()+1)
        self.r = round(self.x_max - self.x_min, 6)
        self.k = math.ceil(1 + (3.32 * math.log10(n)))
        self.l = round(self.r / self.k, self.DecimalCounter())
        self.x_bar = round(sum(self.fiXi()) / n, self.DecimalCounter()+2)
        self.variance = round((sum(self.fiXi2()) - (self.n * self.x_bar ** 2)) / (n - 1), self.DecimalCounter()+2)
        self.S = round(math.sqrt(self.variance), self.DecimalCounter()+2)
        self.sigma1 = round(sum(self.fiXi3()), self.DecimalCounter()+2)
        self.sigma2 = round(sum(self.fiXi4()), self.DecimalCounter()+2)
        self.sigma3 = round(sum(self.fiXi()), self.DecimalCounter()+2)
        self.sigma4 = round(sum(self.fiXi2()), self.DecimalCounter()+2)
        self.skewness = round((self.sigma1 / self.n) / (self.S ** 3), self.DecimalCounter()+2)
        self.kurt = round(((self.sigma2 / self.n) / (self.S ** 4)) - 3, self.DecimalCounter()+2)

    def DecimalCounter(self):
        num1 = 0
        for i in self.array:
            x = str(i)
            if '.' in x:
                y = x.index('.') + 1
                z = x[y:]
                if int(z) == 0 and num1 == 0:
                    num1 = 0
                else:
                    if len(z) > num1:
                        num1 = len(z)
        return num1

    def fi(self):
        a = []
        shadow1 = self.x_min
        for i in range(self.k):
            f = 0
            for j in self.array:
                if shadow1 <= j < shadow1 + self.l:
                    f += 1
            shadow1 += self.l
            a.append(f)
        return a

    def Xi(self):
        b = []
        shadow2 = self.x_min
        for i in range(self.k):
            num2 = round((shadow2 + (shadow2 + self.l)) / 2, 3)
            b.append(num2)
            shadow2 += self.l
        return b

    def ri(self):
        c = []
        for j in self.fi():
            c.append(round(j / self.n, 3))
        return c

    def Fi(self):
        d = []
        num3 = 0
        for q in self.fi():
            num3 += q
            d.append(num3)
        return d

    def gi(self):
        g = []
        num4 = 0
        for i in self.ri():
            num4 += i
            g.append(round(num4, 3))
        return g

    def rows(self):
        h = []
        shadow3 = self.x_min
        for i in range(self.k):
            string1 = f'[{round(shadow3, self.DecimalCounter()+1)}, {round(shadow3 + self.l, self.DecimalCounter()+1)})'
            h.append(string1)
            shadow3 += self.l
        return h

    def fiXi(self):
        m = []
        for i in range(self.k):
            num5 = round(self.fi()[i] * self.Xi()[i], self.DecimalCounter()+1)
            m.append(num5)
        return m

    def fiXi2(self):
        o = []
        for i in range(self.k):
            num5 = round(self.fi()[i] * self.Xi()[i] ** 2, self.DecimalCounter()+1)
            o.append(num5)
        return o

    def fiXi3(self):
        p = []
        for i in range(self.k):
            num6 = round(((self.Xi()[i] - self.x_bar) ** 3) * self.fi()[i], 5)
            p.append(num6)
        return p

    def fiXi4(self):
        t = []
        for i in range(self.k):
            num7 = round(((self.Xi()[i] - self.x_bar) ** 4) * self.fi()[i], 5)
            t.append(num7)
        return t

    def Quantile(self, p):
        shadow4 = self.x_min
        num = self.n * p
        count = 0
        quantile = 0
        while count <= self.k:
            if num <= self.Fi()[count]:
                quantile = shadow4 + ((num - self.Fi()[count-1]) / self.fi()[count]) * self.l
                break
            shadow4 = round(shadow4 + self.l, self.DecimalCounter()+1)
            count += 1
        return round(quantile, self.DecimalCounter()+2)

    def Mod(self):
        num7 = max(self.fi())
        shadow5 = round(self.x_min, self.DecimalCounter()+1)
        a1 = []
        for i in range(self.k):
            if i == 0 and self.fi()[0] == num7:
                mod = {shadow5 + (self.fi()[i]) / ((self.fi()[i]) + (self.fi()[i] - self.fi()[i + 1])) * self.l}
                a1.append(mod)
            elif self.fi()[i] == num7:
                mod = f'{shadow5} + ({self.fi()[i]} - {self.fi()[i - 1]} / {self.fi()[i] - self.fi()[i - 1]} + ' \
                      f'{self.fi()[i] - self.fi()[i + 1]}) * {self.l} ' \
                      f'= {shadow5 + (self.fi()[i] - self.fi()[i - 1]) / ((self.fi()[i] - self.fi()[i - 1]) + (self.fi()[i] - self.fi()[i + 1])) * self.l}'
                a1.append(mod)
            shadow5 = round(shadow5 + self.l, self.DecimalCounter()+1)
        return a1
