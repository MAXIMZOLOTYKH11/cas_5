class Room:
    price = {'одноместный': 2900.00, 'двухместный': 2300.00, 'полулюкс': 3200.00, 'люкс': 4100.00}
    grow_price = {'стандарт': 1.0, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    def __init__(self, number, type, quantity, comfort):
        self.number = number
        self.type = type
        self.quantity = quantity
        self.comfort = comfort
        self.price = self.calc_price()
        self.copyprice = self.calc_price()

    def calc_price(self):
        price = (Room.price[self.type])*(Room.grow_price[self.comfort])*int(self.quantity)
        return price

    def __str__(self):
        s = 'Номер: {} | '.format(self.number)
        s += 'Тип: {} | '.format(self.type)
        s += 'Количество человек: {} | '.format(self.quantity)
        s += 'Степень комфортности: {} | '.format(self.comfort)
        s += 'Цена: {}'.format(self.price)
        return s

    def __repr__(self):
        return self.__str__()


class Choice(Room):

    def __init__(self, number, type, quantity, comfort):
        super(Choice, self).__init__(number=number, type=type, quantity=quantity, comfort=comfort)
        self.tp = 0

    def calc_total_price(self, c, tp, disc):
        if tp == 0:
            pv = 0
        elif tp == 1:
            pv = 280
        else:
            pv = 1000
        if disc == 1:
            k = 0.7
        else:
            k = 1
        total_price = self.price * k + c * pv
        return total_price

    def __str__(self):
        if self.tp == 0:
            stp = 'без_питания'
        elif self.tp == 1:
            stp = 'завтрак'
        else:
            stp = 'полупансион'
        s = 'Номер: {} | '.format(self.number)
        s += 'Тип: {} | '.format(self.type)
        s += 'Количество мест в номере: {} | '.format(self.quantity)
        s += 'Степень комфортности: {} | '.format(self.comfort)
        s += 'Тип питания: ' + stp
        return s

    def __repr__(self):
        return self.__str__()