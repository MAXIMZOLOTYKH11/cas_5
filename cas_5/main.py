from hotel import Room
from hotel import Choice
import io
import random

def rooms():
    k = {}
    t_1 = []
    t_2 = []
    t_3 = []
    t_4 = []
    t_5 = []
    t_6 = []
    with io.open('fund.txt', encoding='utf-8', errors='ignore') as f_fund:
        text = f_fund.readlines()
        for i in text:
            i = i[0:-1]
            i = i.split(' ')
            ir = Room(i[0], i[1], i[2], i[3])
            if ir.quantity == '1':
                t_1.append(ir)
                k[ir.quantity] = t_1
            elif ir.quantity == '2':
                t_2.append(ir)
                k[ir.quantity] = t_2
            elif ir.quantity == '3':
                t_3.append(ir)
                k[ir.quantity] = t_3
            elif ir.quantity == '4':
                t_4.append(ir)
                k[ir.quantity] = t_4
            elif ir.quantity == '5':
                t_5.append(ir)
                k[ir.quantity] = t_5
            elif ir.quantity == '6':
                t_6.append(ir)
                k[ir.quantity] = t_6

    for j in k:
        d = {}
        for w in k[j]:
            if w.price not in d:
                d[w.price] = []
                d[w.price].append(w)
            else:
                d[w.price].append(w)
            d[w.price].reverse()
        k[j] = d
    return k


def people(k):
    booking = {}
    for i in range(1, 100):
        booking[str(i)] = []

    with io.open('booking.txt', encoding='utf-8', errors='ignore') as t_in:
        text = t_in.readlines()
        for i in text:
            try:
                print('...............................................')
                print('Поступила заявка на бронирование:')
                print(i)
                price_hind = []
                i = i.split(' ')
                for j in k[i[4]]:
                    for q in k[i[4]][j]:
                        if q.price == float(i[7]) or q.price < float(i[7]):
                            price_hind.append(q.price)
                i_list = day(i[5], i[6])
                i_set = set(i_list)
            except:
                pass
            kv = {}
            for e in k:
                if i[4] == e:
                    dict_e = {}
                    for p in k[e]:
                        for j in range(len(k[e][p])):
                            u = k[e][p][j]
                            un = k[e][p][j].number

                            set_booking_n = set(booking[un])
                            if len(set_booking_n & i_set) == 0:
                                ukv_0 = Choice(u.number, u.type, u.quantity, u.comfort)
                                ukv_0.tp = 0
                                ukv_0_price = ukv_0.calc_total_price(int(i[4]), ukv_0.tp, 0)
                                dict_e[ukv_0_price] = ukv_0
                                ukv_1 = Choice(u.number, u.type, u.quantity, u.comfort)
                                ukv_1.tp = 1
                                ukv_1_price = ukv_1.calc_total_price(int(i[4]), ukv_1.tp, 0)
                                dict_e[ukv_1_price] = ukv_1
                                ukv_2 = Choice(u.number, u.type, u.quantity, u.comfort)
                                ukv_2.tp = 2
                                ukv_2_price = ukv_2.calc_total_price(int(i[4]), ukv_2.tp, 0)
                                dict_e[ukv_2_price] = ukv_2
                lst_e = list(dict_e.keys())
                lst2_e = []
                for m in lst_e:
                    if m <= float(i[4]) * float(i[7]):
                        lst2_e.append(m)

            try:
                m_l = max(lst2_e)
                bv = dict_e[m_l]
                maybe = random.choice([1, 2, 3, 4])
                if maybe == 4:
                    print('Клиент не согласен.')
                else:
                    print('Найден:  ', bv, m_l, '/сутки')
                    number = bv.number
                    if number in booking:
                        if booking[number] == []:
                            booking[number] = day(i[5], i[6])
                        else:
                            date_of_departure = booking[number][0]
                            if int(date_of_departure) <= int(i[5][:2]):

                                booking[number] = day(i[5], i[6])
                    print('Клиент согласен. Номер забронирован.')
            except:
                print('Предложений по данному запросу нет. В бронировании отказано.')
            kv[e] = dict_e


def day(data, kol_vo):
    day_1 = int(data[:2])
    day_list = []
    day_list.append(day_1)
    for i in range(int(kol_vo)):
        day_1 += 1
        day_list.append(day_1)
        day_list.reverse()
    return day_list


def main():
    people(rooms())


if __name__ == '__main__':
    main()